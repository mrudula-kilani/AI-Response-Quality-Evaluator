from sklearn.metrics.pairwise import cosine_similarity
from agents.model_loader import model

def relevance_score(question, response):

    embeddings = model.encode([question, response])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    score = round(similarity * 10, 2)

    # Generate a simple reasoning
    if score >= 8:
        reason = "The response directly answers the user's question and is highly relevant."
    elif score >= 6:
        reason = "The response is partially relevant but could be more specific."
    else:
        reason = "The response is not sufficiently related to the user's question."

    return {
        "score": score,
        "reason": reason
    }