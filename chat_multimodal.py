from functools import lru_cache

from motor_reglas import generar_respuesta


@lru_cache(maxsize=1)
def obtener_clasificador_visual():
    from clasificador_visual import cargar_clasificador_visual

    return cargar_clasificador_visual()


def responder_consulta(pregunta, ruta_imagen=None):
    respuesta = generar_respuesta(pregunta)

    if ruta_imagen is None:
        return respuesta

    from clasificador_visual import clasificar_imagen

    modelo, categorias = obtener_clasificador_visual()
    categoria = clasificar_imagen(ruta_imagen, modelo, categorias)

    nombres_categorias = {
        "pago_contactless": "Pago sin contacto",
        "tarjeta_fisica": "Tarjeta física",
        "otras": "Otras imágenes",
    }

    return f"{respuesta}\nCategoría predicha: {nombres_categorias[categoria]}"