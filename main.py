from flask import Flask, request
import openai 
from twilio.twiml.messaging_response import MessagingResponse
import os, traceback

app = Flask(__name__)

    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    openai.api_base = "https://openrouter.ai/api/v1"
)

response = openai.ChatCompletion.create(
    model="mistralai/mistral-7b-instruct",  # o un altro modello disponibile
    messages=[
        {"role": "user", "content": messaggio_utente}
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
