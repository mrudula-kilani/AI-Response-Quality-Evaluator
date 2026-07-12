from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def detect_hallucination(response, reference):

    embeddings = model.encode(
        [response, reference]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    if similarity < 0.6:
        return "Possible Hallucination"

    return "No Hallucination Detected"