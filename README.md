AI-Powered Chatbot for Campus Assistance

Overview

The AI-Powered Chatbot for Campus Assistance is a conversational assistant designed to help students navigate campus resources, find event information, and get quick answers to frequently asked questions. Built with Python and SpaCy, this chatbot uses natural language processing (NLP) to understand user queries and provide accurate, real-time responses.

Features

	•	Conversational Capabilities: Handles greetings, affirmations, gratitude, and campus-specific queries.
	•	Campus Navigation: Provides information about locations, such as libraries and cafeterias.
	•	Event Information: Shares details about upcoming campus events.
	•	Modular Design: Easily extendable to add new intents or functionalities.
	•	Web Integration: Includes a Flask-based API for web or mobile integration.

Technologies Used

	•	Programming Language: Python
	•	NLP Library: SpaCy (en_core_web_sm model)
	•	Web Framework: Flask (optional, for API-based interaction)
	•	Data Format: JSON for campus data

Installation

Prerequisites

	1.	Python 3.6+ installed on your system.
	2.	Virtual environment set up for managing dependencies.

Steps

	1.	Clone the repository:

git clone https://github.com/your-username/campus-chatbot.git
cd campus-chatbot


	2.	Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


	3.	Install dependencies:

pip install -r requirements.txt


	4.	Download the SpaCy language model:

python -m spacy download en_core_web_sm

Usage

Command-Line Interface (CLI)

Run the chatbot in CLI mode:

python chatbox_cli.py

Example interaction:

You: Hello
Chatbot: Hello! How can I assist you with your campus-related queries today?

You: Where is the library?
Chatbot: You can find the library in Building A, and the cafeteria in Building B.

Flask-Based Web API

Run the chatbot as a web service:

python chatbox_server.py

Access the API at http://127.0.0.1:5000/chat using POST requests:

curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Where is the event?"}'

Response:

{"response": "The next campus event is the Career Fair, happening on December 5th in the Main Hall."}

Project Structure

├── chatbot_cli.py          # Command-line chatbot implementation
├── chatbox_server.py       # Flask-based web API implementation
├── campus_data.json        # Sample campus data
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── __pycache__/            # Compiled Python files (ignored in Git)

Features in Development

	•	Real-Time Data Integration: Connect to campus databases for live updates.
	•	Enhanced Query Handling: Expand NLP capabilities for more complex questions.
	•	Mobile App Integration: Build a frontend using React Native or Flutter.

Known Issues

	•	The chatbot struggles with ambiguous or highly contextual queries.
	•	Requires integration with a database for scaling beyond static JSON data.

Contribution

Contributions are welcome! Fork the repository, make changes, and submit a pull request.
	1.	Fork the project.
	2.	Create a new feature branch:

git checkout -b feature/your-feature-name


	3.	Commit your changes:

git commit -m "Add your message here"


	4.	Push to the branch:

git push origin feature/your-feature-name


	5.	Open a pull request.

