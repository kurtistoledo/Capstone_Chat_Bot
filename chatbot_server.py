from flask import Flask, request, jsonify
import chatbot_test

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained NLP model
nlp = chatbot_test.load("en_core_web_sm")

# Sample responses for predefined intents
responses = {
    "greeting": "Hello! How can I assist you with your campus-related queries today?",
    "location": "You can find the library in Building A, and the cafeteria in Building B.",
    "event": "The next campus event is the Career Fair, happening on December 5th in the Main Hall.",
    "goodbye": "Goodbye! Feel free to ask if you have more questions.",
    "unknown": "I'm sorry, I didn't understand that. Could you rephrase your question?"
}

# Intent detection function
def detect_intent(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ["hello", "hi"] for token in doc):
        return "greeting"
    elif "location" in user_input or "where" in user_input:
        return "location"
    elif "event" in user_input or "happening" in user_input:
        return "event"
    elif any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return "goodbye"
    else:
        return "unknown"

# Chatbot response function
def chatbot_response(user_input):
    intent = detect_intent(user_input)
    return responses.get(intent, responses["unknown"])

# API route for the chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message field is required"}), 400
    response = chatbot_response(user_input)
    return jsonify({"response": response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
