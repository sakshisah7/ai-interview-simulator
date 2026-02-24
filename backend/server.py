from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample interview questions
questions = [
    {"id": 1, "question": "Tell me about yourself."},
    {"id": 2, "question": "What are your strengths?"},
    {"id": 3, "question": "Explain a challenging project you worked on."}
]

# Home route
@app.route("/")
def home():
    return "AI Interview Simulator Backend Running!"

# Get questions API
@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

# Evaluate answers API
@app.route("/evaluate", methods=["POST"])
def evaluate_answers():
    data = request.json
    answers = data.get("answers", [])

    # Expected keywords for each question
    expected_keywords = [
        ["name", "background", "experience"],
        ["strength", "confidence", "skill"],
        ["challenge", "project", "problem", "solution"]
    ]

    score = 0

    for i, ans in enumerate(answers):
        ans_lower = ans.lower()

        # Check if any keyword matches
        if i < len(expected_keywords):
            if any(keyword in ans_lower for keyword in expected_keywords[i]):
                score += 1

    return jsonify({
        "score": score,
        "total": len(answers)
    })

if __name__ == "__main__":
    app.run(debug=True)