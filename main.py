from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
import openai 
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"
)

@app.route("/")
def index():
    return "ASSI è vivo! 🎉"
    
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    response = MessagingResponse()
    msg = response.message()

    try:
       openai.ChatCompletion.create(
       model="openai/gpt-3.5-turbo",  
       messages=[
        {"role": "system", "content": "Sei ASSI, l'assistente di Silvia."},
        {"role": "user", "content": user_message}
    ]
)
        reply = completion.choices[0].message.content.strip()
    except Exception as e:
        print("⚠️ ERRORE CATTURATO:", e)
        reply = "⚠️ Oops! ASSI sta meditando... Riprova tra poco 🙏"

    msg.body(reply)
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
