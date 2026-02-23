from flask import Flask, jsonify

app = Flask(__name__)

# Sample interview questions
questions = [
    {
        "id": 1,
        "question": "Tell me about yourself."
    },
    {
        "id": 2,
        "question": "What are your strengths?"
    },
    {
        "id": 3,
        "question": "Explain a challenging project you worked on."
    }
]

@app.route("/")
def home():
    return "AI Interview Simulator Backend Running!"

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)