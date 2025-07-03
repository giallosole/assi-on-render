from flask import Flask, request
from openai import OpenAI
from twilio.twiml.messaging_response import MessagingResponse
import os, traceback

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": incoming_msg}
    ]
)
risposta = response['choices'][0]['message']['content']

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
def ask_openrouter(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("⚠️ ERRORE CATTURATO:", e)
        return "⚠️ Qualcosa è andato storto con OpenRouter..."

    return str(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
