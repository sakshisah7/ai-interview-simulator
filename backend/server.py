from flask import render_template
from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer, util
import torch

app = Flask(__name__)

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

questions = [
    {"id": 1, "question": "Tell me about yourself."},
    {"id": 2, "question": "What are your strengths?"},
    {"id": 3, "question": "Explain a challenging project you worked on."}
]

# Ideal answers for comparison
ideal_answers = [
    "My name is Sakshi and I have a background in computer applications with experience in AI and software development.",
    "My strengths include confidence, problem-solving skills, and strong technical knowledge.",
    "I worked on an AI-based project where I faced challenges in model training and successfully solved them."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/evaluate", methods=["POST"])
def evaluate_answers():
    data = request.json
    answers = data.get("answers", [])

    score = 0

    for i, user_answer in enumerate(answers):
        if i < len(ideal_answers):
            embeddings = model.encode([user_answer, ideal_answers[i]], convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
            
            similarity_score = similarity.item()

            # If similarity > 0.5 → consider good answer
            if similarity_score > 0.5:
                score += 1

    return jsonify({
        "score": score,
        "total": len(answers)
    })

if __name__ == "__main__":
    app.run(debug=True)