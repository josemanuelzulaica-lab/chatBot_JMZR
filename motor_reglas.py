
# utilizaremos la base de conocimientos y el interprete de inteciones
from base_conocimientos import intenciones
from interprete_intenciones import identificar_intencion


# se detecta intención y se genera la respusta con base en la base de conocimientos
def generar_respuesta(pregunta):
    intencion = identificar_intencion(pregunta)
    if intencion is not None:
        return intenciones[intencion]["respuesta"]

    # Si no se puede detectar la inteción que tiene el cliente
    return (
        "Lo siento, no logré entender tu duda. "
        "Puedo ayudarte con dudas sobre pagos, intereses, "
        "fechas de corte y tarjetas de crédito."
    )
