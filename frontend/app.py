import requests

# Get questions
response = requests.get("http://127.0.0.1:5000/questions")
questions = response.json()

print("\nAI Interview Simulator\n")

user_answers = []

for q in questions:
    print(f"\nQuestion {q['id']}: {q['question']}")
    answer = input("Your Answer: ")
    user_answers.append(answer)

# Send answers to backend for evaluation
evaluation_response = requests.post(
    "http://127.0.0.1:5000/evaluate",
    json={"answers": user_answers}
)

result = evaluation_response.json()

print("\nInterview Completed!\n")
print(f"Final Score: {result['score']}/{result['total']}")

if result["score"] == result["total"]:
    print("Excellent performance! 🌟")
elif result["score"] >= 2:
    print("Good job! Keep improving 👍")
else:
    print("You need to elaborate more in your answers.")