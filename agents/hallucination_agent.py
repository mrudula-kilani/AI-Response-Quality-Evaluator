from sklearn.metrics.pairwise import cosine_similarity

from agents.model_loader import model
def detect_hallucination(response, reference):

    embeddings = model.encode(
        [response, reference]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    if similarity < 0.85:
        return "Possible Hallucination"

    return "No Hallucination Detected"