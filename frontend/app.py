import requests

response = requests.get("http://127.0.0.1:5000/questions")
questions = response.json()

print("\nAI Interview Simulator\n")

answers = []

for q in questions:
    print(f"\nQuestion {q['id']}: {q['question']}")
    user_answer = input("Your Answer: ")
    
    answers.append({
        "question": q["question"],
        "answer": user_answer
    })

print("\nInterview Completed!\n")
print("Your Answers Summary:\n")

for i, item in enumerate(answers, start=1):
    print(f"{i}. {item['question']}")
    print(f"   Your Answer: {item['answer']}\n")