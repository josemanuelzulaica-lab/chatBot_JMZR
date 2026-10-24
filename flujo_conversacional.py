from motor_reglas import generar_respuesta

def iniciar_chatbot():

    print("asistente : Hola este chat es para poder responder dudas sobre tus tarjetas de crédito.")
    print("Puede preguntar sobre pagos, intereses y alguno otros temas.")
    print("Escribe 'salir' para terminar la conversación.")

    while True:

        pregunta = input("\nCliente: ").strip()

        # cerrar la sesión del cliente cuando ha terminado
        if pregunta.lower() == "salir":
            print("asistente: Gracias por tu visita")
            break

        # manejo cuando el cliente no ha escrito nada
        if not pregunta:
            print("asistente: Por favor, escribe tu duda.")
            continue

        # aplicar motor de reglas para responder
        respuesta = generar_respuesta(pregunta)

        print("asistente:", respuesta)
