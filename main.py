from flask import Flask, request
import os
import httpx
from twilio.twiml.messaging_response import MessagingResponse

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

app = Flask(__name__)

@app.route("/")
def index():
    return "ASSI è vivo! 🎉"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    resp = MessagingResponse()
    msg = resp.message()

try:
        prompt = f"""Rispondi in italiano come ASSI, l'assistente digitale di Silvia – consulente, coach e docente.
Usa empatia, professionalità e un tocco di ironia.
Rispondi al messaggio: {incoming_msg}"""

        incoming_msg = request.form.get('Body', '')
        sender = request.form.get('From', '')
        
if not incoming_msg:
return "Messaggio vuoto", 400

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openrouter/openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": incoming_msg}
            ]
        }

        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()

        reply = response.json()["choices"][0]["message"]["content"]

        print(f"Messaggio da {sender}: {incoming_msg}")
        print(f"Risposta: {reply}")

return reply, 200

except Exception as e:
        print(f"⚠️ ERRORE CATTURATO: {str(e)}")
        return "⚠️ Oops! ASSI sta meditando... Riprova tra poco 🙏", 200

return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
