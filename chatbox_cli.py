import spacy

# Load pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# Sample responses for predefined intents
responses = {
    "greeting": "Hello! How can I assist you with your campus-related queries today?",
    "affirmation": "Great! Let me know how I can assist you further.",
    "location": "You can find the library in Building A, and the cafeteria in Building B.",
    "event": "The next campus event is the Career Fair, happening on December 5th in the Main Hall.",
    "gratitude": "You're welcome! Let me know if there's anything else I can help you with.",
    "goodbye": "Goodbye! Feel free to ask if you have more questions.",
    "unknown": "I'm sorry, I didn't understand that. Could you rephrase your question?"
}

# Intent detection function
def detect_intent(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ["hello", "hi"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["yes", "sure", "okay"] for token in doc):
        return "affirmation"
    elif "location" in user_input or "where" in user_input:
        return "location"
    elif "event" in user_input or "happening" in user_input:
        return "event"
    elif any(token.lemma_ in ["thank", "thanks"] for token in doc):
        return "gratitude"
    elif any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return "goodbye"
    else:
        return "unknown"

# Chatbot interaction function
def chatbot_response(user_input):
    intent = detect_intent(user_input)
    return responses.get(intent, responses["unknown"])

# Main function to interact with the chatbot
def main():
    print("Welcome to the Campus Assistance Chatbot!")
    print("Type 'exit' or 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Feel free to come back anytime.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
