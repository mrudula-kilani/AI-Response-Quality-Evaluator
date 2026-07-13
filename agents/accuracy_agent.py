from sklearn.metrics.pairwise import cosine_similarity

from agents.model_loader import model
def accuracy_score(response, reference):

    embeddings = model.encode(
        [response, reference]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity * 10, 2)