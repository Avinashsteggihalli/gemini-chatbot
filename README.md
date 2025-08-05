# Gemini Chatbot Web App 💬✨

This is a lightweight web-based chatbot powered by **Google's Gemini 2.5 Pro** using the `google-generativeai` Python package. The chatbot runs on a simple Flask server and features:

- 🔒 API key storage via `config.py`
- 🔁 Retry mechanism for failed requests
- 💬 Chat history logging
- 🖱️ Submit messages with Enter key
- 🌐 Web UI with Flask + HTML
- 🚀 Ready to deploy on GitHub/Render

---

## 🛠 How to Run Locally

### 1. Clone this Repository
```bash
git clone https://github.com/YOUR_USERNAME/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Set Your API Key
Create a file named `config.py` and add your Gemini API key like this:

```python
API_KEY = "your-gemini-api-key-here"
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

Then visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧪 Technologies Used

- Python 3.12
- Flask
- Google Generative AI (Gemini)
- HTML/CSS (Frontend)

---

## 📂 Project Structure

```
├── app.py            # Flask backend
├── config.py         # API key storage
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # Frontend HTML
├── static/           # CSS (optional)
│   └── style.css
└── README.md         # You're reading it
```

---

## 🧠 Notes

- Be sure to use a valid API key from [Google AI Studio](https://makersuite.google.com/app).
- Retry and error handling is already built-in.
- You can host this on platforms like **Render**, **Railway**, or **Heroku**.

---

## 📬 Contact

Built by [Avinash S Teggihalli](https://github.com/Avinashsteggihalli)
