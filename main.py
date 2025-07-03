from flask import Flask, request
from openai import OpenAI
from twilio.twiml.messaging_response import MessagingResponse
import os, traceback

app = Flask(__name__)

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key  = os.environ.get("OPENROUTER_API_KEY")
)

@app.route("/")
def home():
    return "✅ ASSI è online tramite OpenRouter!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.values.get("Body", "")
    reply = MessagingResponse()

    messages = [
        {"role": "system", "content": "Rispondi come ASSI, assistente di Silvia: empatico e con ironia."},
        {"role": "user",   "content": msg}
    ]

    try:
        resp = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )
        reply.message(resp.choices[0].message.content.strip())
    except Exception:
        traceback.print_exc()
        reply.message("⚠️ ASSI sta preparando la prossima risposta... Riprova fra poco")

    return str(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
