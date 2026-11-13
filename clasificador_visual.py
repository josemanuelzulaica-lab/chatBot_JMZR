import json
from pathlib import Path

from tensorflow import keras


def cargar_clasificador_visual(carpeta=None):
    if carpeta is None:
        carpeta = Path(__file__).resolve().parent / "modelo_visual"
    else:
        carpeta = Path(carpeta)

    modelo = keras.models.load_model(
        carpeta / "clasificador_visual.keras",
        compile=False,
    )
    categorias = json.loads(
        (carpeta / "categorias.json").read_text(encoding="utf-8")
    )
    return modelo, categorias


def clasificar_imagen(ruta_imagen, modelo, categorias):
    with keras.utils.load_img(
        ruta_imagen,
        color_mode="rgb",
        target_size=(224, 224),
        interpolation="bilinear",
    ) as imagen:
        pixeles = keras.utils.img_to_array(imagen)

    puntajes = modelo.predict(pixeles[None, ...], verbose=0)[0]
    return categorias[int(puntajes.argmax())]