from sklearn.metrics.pairwise import cosine_similarity
from agents.model_loader import model

def accuracy_score(response, reference):

    embeddings = model.encode([response, reference])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    score = round(similarity * 10, 2)

    # Generate supporting evidence
    if score >= 9:
        evidence = "The response closely matches the reference answer."
    elif score >= 7:
        evidence = "The response is mostly accurate but differs slightly from the reference."
    else:
        evidence = "The response does not sufficiently match the reference answer."

    return {
        "score": score,
        "evidence": evidence
    }