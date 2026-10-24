
import unicodedata
from nltk.tokenize import word_tokenize
from base_conocimientos import intenciones

# Etapa de Eliminación de stopwords, se eliminan palabras que no aportan valor como: que, del, puedes, quiero, etc
palabras_comunes = {
    "que", "es", "la", "el", "los", "las",
    "de", "del", "mi", "mis", "tu", "un",
    "una", "para", "por", "con", "en",
    "me", "puedes", "quiero", "quisiera",
    "saber", "necesito", "ayuda", "como",
    "cuando", "si", "se", "a"
}

# Etapa de Lematización, transformando palabras para poder ampliar el margen de entendimiento
lema = {
    "pagar": "pago",
    "pagos": "pago",
    "intereses": "interes",
    "funcionan": "funcionamiento",
    "comprar": "compra",
    "compras": "compra",
    "tiendas": "tienda",
    "activo": "activar",
    "activacion": "activar",
    "deuda": "saldo",
    "codigo": "cvv",
    "seguridad": "cvv",
    "dinamico": "cvv"
}

# Etapa de normalización y tokenizacion donde convertimos a minusculas, eliminamos acentos, los signos de puntuación y se divide la frase en palabras mediante tokenización.
def procesar_pregunta(texto):

    texto = texto.lower()
    texto = "".join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )

    texto = "".join(
        caracter for caracter in texto
        if caracter.isalnum() or caracter.isspace()
    )
    
            #se regresan tokenizadas las dudas de los clientes en palabras
    return word_tokenize(texto, language="spanish")


# se detectan palabras clave que nos ayudan a detectar la intención
def obtener_palabras_clave(texto):

    palabras = procesar_pregunta(texto)
    palabras_clave = []

    for palabra in palabras:
        if palabra not in palabras_comunes:
            palabra = lema.get(palabra, palabra)
            palabras_clave.append(palabra)

    return palabras_clave


# Etapa de Clasificación de intención, comparando palabras y seleccionando la intención que supere el 70% de coincidencia
def identificar_intencion(pregunta):

    palabras_cliente = set(obtener_palabras_clave(pregunta))

    mejor_intencion = None
    mayor_coincidencia = 0

    for nombre_intencion, datos in intenciones.items():

        for duda in datos["dudas"]:

            palabras_duda = set(obtener_palabras_clave(duda))

            if not palabras_duda:
                continue

            coincidencias = len(palabras_cliente & palabras_duda)
            porcentaje = coincidencias / len(palabras_duda)

            if porcentaje > mayor_coincidencia:
                mayor_coincidencia = porcentaje
                mejor_intencion = nombre_intencion
    # aqui definimmos el grade de coincidencia deseado
    if mayor_coincidencia >= 0.70:
        return mejor_intencion
    return None
