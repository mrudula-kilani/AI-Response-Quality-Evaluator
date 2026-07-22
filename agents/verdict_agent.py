def overall_verdict(relevance, accuracy, completeness, hallucination):

    overall_score = round(
        (relevance + accuracy + completeness) / 3,
        2
    )

    if hallucination == "No Hallucination":

        if overall_score >= 9:
            verdict = "Excellent"
            recommendation = "The response is highly relevant, accurate, complete, and trustworthy."

        elif overall_score >= 7:
            verdict = "Good"
            recommendation = "The response is reliable but could include more details."

        else:
            verdict = "Needs Improvement"
            recommendation = "The response should be improved for better quality."

    else:

        verdict = "Poor"
        recommendation = "The response may contain hallucinated or unsupported information."

    return {
        "overall_score": overall_score,
        "verdict": verdict,
        "recommendation": recommendation
    }