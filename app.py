from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Obtén las credenciales de Twilio y el número de teléfono de Twilio de las variables de entorno
TWILIO_ACCOUNT_SID = os.environ.get('AC148063f3ed9416660faafcd76e73fdcb')
TWILIO_AUTH_TOKEN = os.environ.get('1016ca53ebb4d2d8d5f26d1a8bed6508')
TWILIO_PHONE_NUMBER = os.environ.get('+14155238886')

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtiene el cuerpo del mensaje y el número de teléfono del remitente
    message_body = request.form['Body']
    sender_phone_number = request.form['From']
    
    # Tu lógica para procesar el mensaje y generar una respuesta
    # En este ejemplo, simplemente devolvemos un mensaje de agradecimiento
    response_message = "¡Gracias por contactar a nuestra tienda de ropa! Estamos procesando tu mensaje."
    
    # Crea una respuesta usando Twilio's MessagingResponse
    response = MessagingResponse()
    response.message(response_message)
    
    return str(response)

if __name__ == "__main__":
    # Ejecuta la aplicación en el puerto 5000
    app.run(debug=True, port=5000)
