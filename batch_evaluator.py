import pandas as pd

from agents.relevance_agent import relevance_score
from agents.accuracy_agent import accuracy_score
from agents.hallucination_agent import detect_hallucination
from agents.completeness_agent import completeness_score
from agents.verdict_agent import overall_verdict


def evaluate_batch(df):

    results = []

    for _, row in df.iterrows():

        question = row["Question"]
        reference = row["Reference"]
        response = row["Response"]

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

        results.append({

            "Question": question,
            "Reference": reference,
            "Response": response,

            "Relevance Score": round(relevance["score"], 2),
            "Relevance Reason": relevance["reason"],

            "Accuracy Score": round(accuracy["score"], 2),
            "Accuracy Evidence": accuracy["evidence"],

            "Hallucination": hallucination["status"],
            "Hallucination Reason": hallucination["reason"],

            "Completeness Score": round(completeness["score"], 2),
            "Completeness Feedback": completeness["feedback"],
            "Missing Points": ", ".join(completeness["missing_points"]),

            "Overall Score": verdict["overall_score"],
            "Verdict": verdict["verdict"],
            "Summary": " | ".join(verdict["summary"])

        })

    return pd.DataFrame(results)