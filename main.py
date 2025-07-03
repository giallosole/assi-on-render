rom flask import Flask, request
from openai import OpenAI
from twilio.twiml.messaging_response import MessagingResponse
import os
import traceback

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "✅ ASSI è online!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '')
    reply = MessagingResponse()

    prompt = f"""Rispondi in italiano come ASSI, l'assistente digitale di Silvia – consulente, coach e docente.
    Usa empatia, professionalità e un tocco di ironia.
    Rispondi al messaggio: {incoming_msg}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.8
        )
        risposta = response.choices[0].message.content.strip()
        reply.message(risposta)
    except Exception as e:
        print("🛑 ERRORE GPT:")
        traceback.print_exc()
        reply.message("⚠️ Ops! ASSI sta meditando... riprova tra poco 🌙")

    return str(reply)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
