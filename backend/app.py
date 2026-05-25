# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from gemini_service import generate_response

# Create Flask app
app = Flask(__name__)

# Enable CORS so frontend can talk to backend
CORS(app)


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "AI Chatbot Backend is Running!"
    })


# -----------------------------
# Chat Route
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    try:
        # Get JSON data sent from frontend
        data = request.get_json()

        # Extract user message
        user_message = data.get("message")

        # Check if message is empty
        if not user_message:
            return jsonify({
                "error": "Message is required"
            }), 400

        # Generate AI response
        ai_response = generate_response(user_message)

        # Return response to frontend
        return jsonify({
            "response": ai_response
        })

    except Exception as e:

        # Handle unexpected errors
        return jsonify({
            "error": str(e)
        }), 500


# -----------------------------
# Run Flask Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)