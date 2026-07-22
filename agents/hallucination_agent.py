from sklearn.metrics.pairwise import cosine_similarity
from agents.model_loader import model

def detect_hallucination(response, reference):

    embeddings = model.encode([response, reference])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    if similarity >= 0.8:
        return {
            "status": "No Hallucination",
            "reason": "The response is well supported by the reference answer."
        }
    else:
        return {
            "status": "Possible Hallucination",
            "reason": "The response contains information that is not sufficiently supported by the reference answer."
        }