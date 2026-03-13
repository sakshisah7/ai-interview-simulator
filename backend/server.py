from flask import Flask, jsonify, request, render_template
from sentence_transformers import SentenceTransformer, util
import torch

app = Flask(__name__)

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Interview questions
questions = [
    {"id": 1, "question": "Tell me about yourself."},
    {"id": 2, "question": "What are your strengths?"},
    {"id": 3, "question": "Explain a challenging project you worked on."}
]

# Ideal answers used for comparison
ideal_answers = [
    "My name is Sakshi and I have a background in computer applications with experience in AI and software development.",
    "My strengths include confidence, problem-solving skills, and strong technical knowledge.",
    "I worked on an AI-based project where I faced challenges in model training and successfully solved them."
]

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API to fetch interview questions
@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)


# AI evaluation API
@app.route("/evaluate", methods=["POST"])
def evaluate_answers():

    data = request.json
    answers = data.get("answers", [])

    score = 0
    details = []

    for i, user_answer in enumerate(answers):

        if i < len(ideal_answers):

            embeddings = model.encode(
                [user_answer, ideal_answers[i]],
                convert_to_tensor=True
            )

            similarity = util.pytorch_cos_sim(
                embeddings[0],
                embeddings[1]
            )

            similarity_score = similarity.item()

            # Save similarity + feedback
            details.append({
                "question": questions[i]["question"],
                "similarity": round(similarity_score * 100, 2),
                "feedback": (
                    "Excellent answer!" if similarity_score > 0.8 else
                    "Good answer but could include more details." if similarity_score > 0.6 else
                    "Partially relevant answer." if similarity_score > 0.4 else
                    "Answer not relevant to the question."
                )
            })

            # scoring threshold
            if similarity_score > 0.5:
                score += 1

    return jsonify({
        "score": score,
        "total": len(answers),
        "details": details
    })


if __name__ == "__main__":
    app.run(debug=True)
