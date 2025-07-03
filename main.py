from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
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
        completion = client.chat.completions.create(
            model="openrouter/gpt-3.5-turbo",  # oppure "mistralai/mistral-7b-instruct"
            messages=[
                {"role": "user", "content": incoming_msg}
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
