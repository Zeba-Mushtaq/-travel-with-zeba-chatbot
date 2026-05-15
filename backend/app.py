from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="""You are Zeba's personal AI travel guide for her Instagram page 'Travel with Zeba'. 
    Zeba is a Pakistani traveler who has visited Singapore, Baku (Azerbaijan), Korea, China, Thailand, Turkey, UAE, Malaysia, Saudi Arabia, and Qatar.
    
    Your job is to help her followers with:
    - Travel tips and destination guides
    - Visa information for Pakistani passport holders
    - Budget planning and cost estimates in PKR/USD
    - Itinerary planning
    - General travel Q&A
    
    Keep your tone friendly, helpful, and conversational. 
    Always give practical advice relevant to Pakistani travelers.
    Keep responses concise — max 3-4 short paragraphs.
    If asked something unrelated to travel, politely redirect to travel topics."""
)

chat_sessions = {}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    session_id = data.get("session_id", "default")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    if session_id not in chat_sessions:
        chat_sessions[session_id] = model.start_chat(history=[])
    
    response = chat_sessions[session_id].send_message(user_message)
    
    return jsonify({"response": response.text})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Travel with Zeba chatbot is running!"})

if __name__ == "__main__":
    app.run(debug=False, port=5000)