import streamlit as st

from agents.relevance_agent import relevance_score
from agents.accuracy_agent import accuracy_score
from agents.hallucination_agent import detect_hallucination
from agents.verdict_agent import overall_verdict

st.set_page_config(page_title="AI Response Quality Evaluator")

st.title("AI Response Quality Evaluator")

question = st.text_area("Question")
response = st.text_area("AI Response")
reference = st.text_area("Reference Answer")

if st.button("Evaluate"):

    if question and response and reference:

        # Evaluate relevance
        relevance = relevance_score(
            question,
            response
        )

        # Evaluate accuracy
        accuracy = accuracy_score(
            response,
            reference
        )

        # Detect hallucination
        hallucination = detect_hallucination(
            response,
            reference
        )

        # Generate overall verdict
        verdict = overall_verdict(
            relevance["score"],
            accuracy["score"],
            hallucination["status"]
        )

        # Display results
        st.subheader("Evaluation Results")

        st.metric(
            "Relevance Score",
            f"{relevance['score']:.2f}/10"
        )

        st.write("**Reason:**")
        st.write(relevance["reason"])

        st.metric(
            "Accuracy Score",
            f"{accuracy['score']:.2f}/10"
        )

        st.write("**Evidence:**")
        st.write(accuracy["evidence"])

        st.write("**Hallucination Status:**")
        st.write(hallucination["status"])

        st.write("**Reason:**")
        st.write(hallucination["reason"])

        st.subheader("Overall Verdict")

        st.metric(
            "Overall Score",
            f"{verdict['overall_score']:.2f}/10"
        )

        st.write("**Verdict:**")
        st.write(verdict["verdict"])

        st.write("**Recommendation:**")
        st.write(verdict["recommendation"])

    else:
        st.warning("Please fill in all the fields before evaluating.")