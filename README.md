# 🤖 AI Customer Support Chatbot

A beginner-friendly customer support chatbot built with **Python + Flask + HTML/CSS/JavaScript**.

## ✨ Features

- 💬 Interactive web chat interface
- 🔎 Fuzzy matching for common customer questions
- 📦 Order and delivery support
- 🔄 Returns and refund guidance
- 💳 Payment troubleshooting
- 🛟 Fallback response for unknown questions
- ❤️ Simple health-check API
- 📱 Responsive interface

## 🗂️ Project Structure

```text
ai-customer-support-chatbot-v2/
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── knowledge_base.json
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## 🚀 Run Locally

### 1. Install Python
Make sure Python 3.10+ is installed.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

### 4. Open the chatbot

Visit `http://127.0.0.1:5000` in your browser.

## 🧠 How It Works

1. The user enters a support question.
2. JavaScript sends the question to Flask through `/api/chat`.
3. The chatbot normalizes the text and compares it with questions in the local knowledge base.
4. The closest matching answer is returned.
5. The web interface displays the response instantly.

## 🔧 Customization

Add new customer questions and answers in `data/knowledge_base.json`. You can create additional categories such as account, cancellation, warranty, or technical support.

## ⚠️ Note

This project is a portfolio/demo chatbot. The sample answers are generic and should be replaced with verified information for a real business.
