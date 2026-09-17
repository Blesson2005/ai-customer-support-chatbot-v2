from flask import Flask, jsonify, render_template, request
from chatbot import CustomerSupportBot

app = Flask(__name__)
bot = CustomerSupportBot("data/knowledge_base.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()

    if not message:
        return jsonify({"reply": "Please type a message so I can help you."}), 400

    result = bot.get_response(message)
    return jsonify(result)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "AI Customer Support Chatbot"})

if __name__ == "__main__":
    app.run(debug=True)
