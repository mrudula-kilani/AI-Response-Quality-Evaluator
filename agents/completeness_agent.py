from sklearn.metrics.pairwise import cosine_similarity
from agents.model_loader import model

def completeness_score(question, response):

    embeddings = model.encode([question, response])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    score = round(similarity * 10, 2)

    if score >= 9:
        feedback = "The response completely addresses the question."
    elif score >= 7:
        feedback = "The response covers most parts of the question but could include more details."
    else:
        feedback = "The response does not fully answer the question."

    return {
        "score": score,
        "feedback": feedback
    }