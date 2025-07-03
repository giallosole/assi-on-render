from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ ASSI è online e pronto a rispondere su WhatsApp!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "")
    reply = MessagingResponse()

    try:
        prompt = f"""Rispondi in italiano come ASSI, l'assistente digitale di Silvia – consulente, coach e docente.
Usa empatia, professionalità e un tocco di ironia.
Rispondi al messaggio: {incoming_msg}"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        reply_msg = response.choices[0].message.content.strip()
        reply.message(reply_msg)
    except Exception as e:
        reply.message("Ops! Qualcosa è andato storto 🧯")

    return str(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
