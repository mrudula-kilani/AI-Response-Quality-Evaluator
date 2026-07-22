def overall_verdict(relevance, accuracy, hallucination):

    overall_score = round((relevance + accuracy) / 2, 2)

    if hallucination == "No Hallucination":
        if overall_score >= 9:
            verdict = "Excellent"
            recommendation = "The response is highly relevant, accurate, and trustworthy."
        elif overall_score >= 7:
            verdict = "Good"
            recommendation = "The response is mostly reliable with minor improvements possible."
        else:
            verdict = "Needs Improvement"
            recommendation = "The response should be improved for better relevance and accuracy."
    else:
        verdict = "Poor"
        recommendation = "The response may contain hallucinated or unsupported information."

    return {
        "overall_score": overall_score,
        "verdict": verdict,
        "recommendation": recommendation
    }