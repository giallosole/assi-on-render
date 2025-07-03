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

        def chiedi_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "openrouter/openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei ASSI, l'assistente di Silvia."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response['choices'][0]['message']['content'].strip()
        msg.body(reply)

    except Exception as e:
        print("⚠️ ERRORE CATTURATO:", e)
        msg.body("⚠️ Riprova tra poco 🙏")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
