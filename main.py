from flask import Flask, request
from openai import OpenAI
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "✅ ASSI è online e pronto a rispondere su WhatsApp!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '')
    reply = MessagingResponse()

    # Prompt con tono personalizzato
    messages = [
        {
            "role": "system",
            "content": "Rispondi in italiano come ASSI, l'assistente digitale di Silvia – consulente, coach e docente. Usa empatia, professionalità e un tocco di ironia."
        },
        {
            "role": "user",
            "content": incoming_msg
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.8
        )
        risposta = response.choices[0].message.content.strip()
        reply.message(risposta)
    except Exception as e:
        print("⚠️ ERRORE CATTURATO:", e)
        reply.message("⚠️ Oops! ASSI sta meditando... Riprova tra poco 🙏")

    return str(reply)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
