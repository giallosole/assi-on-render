import os
import openai
from flask import Flask, request
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
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo-instruct",
             messages=[
        {"role": "system", "content": "Sei ASSI, l'assistente di Silvia."},
        {"role": "user", "content": user_message}
    ]
)
 reply = completion.choices[0].message.content.strip()
except Exception as e:
        print("⚠️ ERRORE CATTURATO:", e)
        reply = "⚠️ Riprova tra poco 🙏"       
        reply = response['choices'][0]['message']['content']
        msg.body(reply)

except Exception as e:
        msg.body(f"⚠️ ERRORE CATTURATO: {str(e)}")

return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
