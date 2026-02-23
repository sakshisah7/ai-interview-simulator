from flask import Flask, jsonify, request

app = Flask(__name__)

questions = [
    {"id": 1, "question": "Tell me about yourself."},
    {"id": 2, "question": "What are your strengths?"},
    {"id": 3, "question": "Explain a challenging project you worked on."}
]

@app.route("/")
def home():
    return "AI Interview Simulator Backend Running!"

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/evaluate", methods=["POST"])
def evaluate_answers():
    data = request.json
    answers = data.get("answers", [])

    score = 0

    for ans in answers:
        if len(ans.split()) > 3:
            score += 1

    return jsonify({
        "score": score,
        "total": len(answers)
    })

if __name__ == "__main__":
    app.run(debug=True)