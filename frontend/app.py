import requests

response = requests.get("http://127.0.0.1:5000/questions")
questions = response.json()

print("\nAI Interview Simulator\n")

answers = []
score = 0

for q in questions:
    print(f"\nQuestion {q['id']}: {q['question']}")
    user_answer = input("Your Answer: ")

    # Simple scoring logic
    if len(user_answer.split()) > 3:
        score += 1

    answers.append({
        "question": q["question"],
        "answer": user_answer
    })

print("\nInterview Completed!\n")
print("Your Answers Summary:\n")

for i, item in enumerate(answers, start=1):
    print(f"{i}. {item['question']}")
    print(f"   Your Answer: {item['answer']}\n")

print(f"Final Score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent performance! 🌟")
elif score >= 2:
    print("Good job! Keep improving 👍")
else:
    print("You need to elaborate more in your answers.")