import streamlit as st

from agents.relevance_agent import relevance_score
from agents.accuracy_agent import accuracy_score
from agents.hallucination_agent import detect_hallucination

st.set_page_config(page_title="AI Response Quality Evaluator")

st.title("AI Response Quality Evaluator")

question = st.text_area("Question")

response = st.text_area("AI Response")

reference = st.text_area("Reference Answer")

if st.button("Evaluate"):

    if question and response and reference:

        relevance = relevance_score(
            question,
            response
        )

        accuracy = accuracy_score(
            response,
            reference
        )

        hallucination = detect_hallucination(
            response,
            reference
        )

        st.subheader("Evaluation Results")

        st.metric(
            "Relevance Score",
            f"{relevance:.2f}/10"
        )

        st.metric(
            "Accuracy Score",
            f"{accuracy:.2f}/10"
        )

        st.write(
            "Hallucination Status:",
            hallucination
        )