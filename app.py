import streamlit as st

st.title("AI Response Quality Evaluator")

question = st.text_area("Question")

response = st.text_area("AI Response")

reference = st.text_area("Reference Answer")

if st.button("Evaluate"):
    st.success("Evaluation Started")