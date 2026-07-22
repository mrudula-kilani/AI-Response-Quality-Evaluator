import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agents.relevance_agent import relevance_score
from agents.accuracy_agent import accuracy_score
from agents.hallucination_agent import detect_hallucination
from agents.completeness_agent import completeness_score
from agents.verdict_agent import overall_verdict
from batch_evaluator import evaluate_batch

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    layout="wide"
)

st.title("🤖 AI Response Quality Evaluator")

mode = st.sidebar.radio(
    "Select Evaluation Mode",
    ["Single Response", "Batch Evaluation"]
)

# =====================================================
# SINGLE RESPONSE
# =====================================================

if mode == "Single Response":

    question = st.text_area("Question")
    response = st.text_area("AI Response")
    reference = st.text_area("Reference Answer")

    if st.button("Evaluate"):

        if question and response and reference:

            relevance = relevance_score(question, response)
            accuracy = accuracy_score(response, reference)
            hallucination = detect_hallucination(response, reference)
            completeness = completeness_score(
                question,
                response,
                reference
            )

            verdict = overall_verdict(
                relevance["score"],
                accuracy["score"],
                completeness["score"],
                hallucination["status"]
            )

            st.header("Evaluation Results")

            c1, c2 = st.columns(2)

            with c1:
                st.metric(
                    "Relevance Score",
                    f"{relevance['score']:.2f}/10"
                )
                st.write("**Reason:**")
                st.write(relevance["reason"])

            with c2:
                st.metric(
                    "Accuracy Score",
                    f"{accuracy['score']:.2f}/10"
                )
                st.write("**Evidence:**")
                st.write(accuracy["evidence"])

            c3, c4 = st.columns(2)

            with c3:
                st.metric(
                    "Hallucination",
                    hallucination["status"]
                )
                st.write("**Reason:**")
                st.write(hallucination["reason"])

            with c4:
                st.metric(
                    "Completeness Score",
                    f"{completeness['score']:.2f}/10"
                )
                st.write("**Feedback:**")
                st.write(completeness["feedback"])

            if completeness["missing_points"]:
                st.subheader("Missing Points")

                for point in completeness["missing_points"]:
                    st.write(f"• {point}")

            st.header("Overall Verdict")

            st.metric(
                "Overall Score",
                f"{verdict['overall_score']:.2f}/10"
            )

            st.success(verdict["verdict"])

            st.subheader("Consolidated Reasoning")

            for item in verdict["summary"]:
                st.write(f"• {item}")

        else:
            st.warning("Please fill all fields.")

# =====================================================
# BATCH EVALUATION
# =====================================================

else:

    st.header("Batch Evaluation")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Dataset")
        st.dataframe(df, use_container_width=True)

        if st.button("Run Batch Evaluation"):

            results = evaluate_batch(df)

            st.subheader("Evaluation Results")
            st.dataframe(results, use_container_width=True)

            st.subheader("Summary Dashboard")

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(
                    "Overall",
                    f"{results['Overall Score'].mean():.2f}/10"
                )

            with col2:
                st.metric(
                    "Relevance",
                    f"{results['Relevance Score'].mean():.2f}/10"
                )

            with col3:
                st.metric(
                    "Accuracy",
                    f"{results['Accuracy Score'].mean():.2f}/10"
                )

            with col4:
                st.metric(
                    "Completeness",
                    f"{results['Completeness Score'].mean():.2f}/10"
                )

            with col5:
                st.metric(
                    "Hallucinations",
                    len(
                        results[
                            results["Hallucination"] == "Possible Hallucination"
                        ]
                    )
                )

            csv = results.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇ Download Evaluation Results",
                data=csv,
                file_name="evaluation_results.csv",
                mime="text/csv"
            )

            # =====================================================
            # VISUAL ANALYTICS
            # =====================================================

            st.subheader("📊 Visual Analytics")

            chart_col1, chart_col2 = st.columns(2)

            # -------------------------
            # Bar Chart
            # -------------------------

            with chart_col1:

                scores = {
                    "Relevance": results["Relevance Score"].mean(),
                    "Accuracy": results["Accuracy Score"].mean(),
                    "Completeness": results["Completeness Score"].mean(),
                    "Overall": results["Overall Score"].mean()
                }

                fig1, ax1 = plt.subplots(figsize=(6,4))

                ax1.bar(
                    scores.keys(),
                    scores.values()
                )

                ax1.set_ylim(0, 10)
                ax1.set_ylabel("Average Score")
                ax1.set_title("Average Evaluation Scores")

                st.pyplot(fig1)

            # -------------------------
            # Pie Chart
            # -------------------------

            with chart_col2:

                verdict_counts = results["Verdict"].value_counts()

                fig2, ax2 = plt.subplots(figsize=(5,5))

                ax2.pie(
                    verdict_counts,
                    labels=verdict_counts.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                ax2.set_title("Verdict Distribution")

                st.pyplot(fig2)