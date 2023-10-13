from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    # Obtén el mensaje del cliente
    message_body = request.form['Body']

    # Crea una respuesta
    resp = MessagingResponse()

    # Dependiendo del mensaje del cliente, puedes personalizar las respuestas.
    if "¿Tienes jeans?" in message_body:
        resp.message("¡Sí, tenemos jeans! ¿Estás buscando un estilo específico?")
    elif "¿Cuál es el horario de la tienda?" in message_body:
        resp.message("Nuestro horario es de 9 a.m. a 9 p.m. todos los días.")
    else:
        resp.message("Lo siento, no entendí tu pregunta. ¿Podrías reformularla?")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
