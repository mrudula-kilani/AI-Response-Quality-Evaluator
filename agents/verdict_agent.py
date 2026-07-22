def overall_verdict(relevance, accuracy, completeness, hallucination):

    # Weighted scoring
    relevance_weight = 0.30
    accuracy_weight = 0.40
    completeness_weight = 0.20
    hallucination_weight = 0.10

    hallucination_score = 10 if hallucination == "No Hallucination" else 0

    overall_score = round(
        (relevance * relevance_weight) +
        (accuracy * accuracy_weight) +
        (completeness * completeness_weight) +
        (hallucination_score * hallucination_weight),
        2
    )

    summary = []

    if relevance >= 8:
        summary.append("The response is highly relevant to the question.")
    elif relevance >= 6:
        summary.append("The response is reasonably relevant.")
    else:
        summary.append("The response has low relevance.")

    if accuracy >= 8:
        summary.append("The response is factually accurate.")
    elif accuracy >= 6:
        summary.append("The response is mostly accurate but has minor differences.")
    else:
        summary.append("The response contains factual inaccuracies.")

    if completeness >= 8:
        summary.append("The response covers all important aspects.")
    elif completeness >= 6:
        summary.append("Some important information is missing.")
    else:
        summary.append("The response is incomplete.")

    if hallucination == "No Hallucination":
        summary.append("No hallucinated content was detected.")
    else:
        summary.append("Possible hallucinated content was detected.")

    if overall_score >= 8:
        verdict = "Pass"
    elif overall_score >= 6:
        verdict = "Needs Improvement"
    else:
        verdict = "Fail"

    return {
        "overall_score": overall_score,
        "verdict": verdict,
        "summary": summary
    }