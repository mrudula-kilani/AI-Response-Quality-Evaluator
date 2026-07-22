import pandas as pd

from agents.relevance_agent import relevance_score
from agents.accuracy_agent import accuracy_score
from agents.hallucination_agent import detect_hallucination

# Load benchmark dataset
df = pd.read_csv("data/benchmark.csv")
total_relevance = 0
total_accuracy = 0
hallucination_count = 0
print("=" * 80)
print("AI RESPONSE QUALITY EVALUATOR - VALIDATION")
print("=" * 80)

for index, row in df.iterrows():

    print(f"\nTest Case {index + 1}")

    question = row["Question"]
    reference = row["Reference"]
    response = row["Response"]

    relevance = relevance_score(question, response)
    accuracy = accuracy_score(response, reference)
    hallucination = detect_hallucination(response, reference)
    total_relevance += relevance["score"]
    total_accuracy += accuracy["score"]

    if hallucination["status"] == "Possible Hallucination":
        hallucination_count += 1

    print(f"Question       : {question}")
    print(f"Response       : {response}")

    print(f"Relevance      : {relevance['score']}/10")
    print(f"Accuracy       : {accuracy['score']}/10")
    print(f"Hallucination  : {hallucination['status']}")

    print("-" * 80)

average_relevance = total_relevance / len(df)
average_accuracy = total_accuracy / len(df)

print("\n" + "=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)

print(f"Total Test Cases        : {len(df)}")
print(f"Average Relevance Score : {average_relevance:.2f}/10")
print(f"Average Accuracy Score  : {average_accuracy:.2f}/10")
print(f"Hallucinations Detected : {hallucination_count}")

print("\nValidation Complete.")