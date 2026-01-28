from flask import Blueprint, jsonify, request
from rapidfuzz import fuzz
import re

api = Blueprint("api", __name__)

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


@api.route("/detect-brands/", methods=["POST"])
def detect_brands():
    data = request.get_json()

    text = data.get("text", "")
    targets = data.get("targets", [])
    threshold = data.get("threshold", 80)

    normalized_text = normalize(text)

    best_match = None
    best_score = 0
    matched_substring = ""

    for target in targets:
        normalized_target = normalize(target)
        score = fuzz.partial_ratio(normalized_text, normalized_target)

        if score > best_score:
            best_score = score
            best_match = target

            words = text.split()
            best_word = max(
                words,
                key=lambda w: fuzz.partial_ratio(normalize(w), normalized_target)
            )
            matched_substring = best_word

    matched = best_score >= threshold
    confidence = best_score

    if matched:
        reason = f"{best_match} is similar to {matched_substring}"
    else:
        reason = "No sufficiently similar brand found"

    return jsonify({
        "data": {
            "matched": matched,
            "confidence": confidence,
            "reason": reason
        }
    })



@api.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello from API router"
    })

@api.route("/users", methods=["GET"])
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

@api.route("/users", methods=["POST"])
def create_user():
    data = request.json
    return jsonify({
        "id": 3,
        "name": data["name"],
        "qdesc": data["qdesc"],
    }), 201


