from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Obtén las credenciales de Twilio y el número de teléfono de Twilio de las variables de entorno
TWILIO_ACCOUNT_SID = os.environ.get('AC148063f3ed9416660faafcd76e73fdcb')
TWILIO_AUTH_TOKEN = os.environ.get('1016ca53ebb4d2d8d5f26d1a8bed6508')
TWILIO_PHONE_NUMBER = os.environ.get('+14155238886')


def generate_response(message_body):
    # Lógica para generar respuestas basadas en el mensaje del cliente
    if "horario" in message_body.lower():
        return "Nuestro horario de atención es de lunes a viernes de 9 AM a 6 PM."
    elif "productos" in message_body.lower():
        return "Tenemos una variedad de productos de alta calidad. ¿Hay algo específico que estás buscando?"
    elif "ofertas" in message_body.lower():
        return "¡Consulta nuestras últimas ofertas en nuestro sitio web!"
    else:
        return "Gracias por tu mensaje. Estamos revisando tu consulta y te responderemos pronto."

@app.route('/webhook', methods=['POST'])
def webhook():
    message_body = request.form['Body']
    sender_phone_number = request.form['From']
    
    response_message = generate_response(message_body)
    
    response = MessagingResponse()
    response.message(response_message)
    
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
