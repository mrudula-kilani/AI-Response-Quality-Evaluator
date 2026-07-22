from sklearn.metrics.pairwise import cosine_similarity
from agents.model_loader import model


def completeness_score(question, response, reference):

    embeddings = model.encode([question, response, reference])

    question_similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    reference_similarity = cosine_similarity(
        [embeddings[2]],
        [embeddings[1]]
    )[0][0]

    similarity = (question_similarity + reference_similarity) / 2

    score = round(similarity * 10, 2)

    # Identify missing points
    reference_points = [point.strip() for point in reference.split(".") if point.strip()]

    missing_points = []

    for point in reference_points:
        if point.lower() not in response.lower():
            missing_points.append(point)

    if score >= 9:
        feedback = "The response completely addresses the question."

    elif score >= 7:
        if missing_points:
            feedback = (
                "The response covers most parts of the question but is missing: "
                + ", ".join(missing_points)
            )
        else:
            feedback = "The response covers most parts of the question."

    else:
        if missing_points:
            feedback = (
                "The response does not fully answer the question. Missing: "
                + ", ".join(missing_points)
            )
        else:
            feedback = "The response does not fully answer the question."

    return {
        "score": score,
        "feedback": feedback,
        "missing_points": missing_points
    }