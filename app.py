from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
import json
import time
from datetime import datetime
from google.api_core.exceptions import ResourceExhausted

# Load API key
with open("config.json") as f:
    config = json.load(f)
genai.configure(api_key=config["api_key"])

model = genai.GenerativeModel("models/gemini-2.5-pro")
chat = model.start_chat(history=[])

app = Flask(__name__)

# log file
log_file = "chat_log.json"

def log_chat(user, bot):
    entry = {
        "time": datetime.now().isoformat(),
        "user": user,
        "gemini": bot
    }
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except:
        pass

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "Please ask something."})
    
    try:
        response = chat.send_message(user_message)
        bot_reply = response.text
        log_chat(user_message, bot_reply)
        return jsonify({"reply": bot_reply})
    except ResourceExhausted:
        return jsonify({"reply": "Too many requests, please slow down."})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
