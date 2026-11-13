from collections import Counter

from sklearn.model_selection import train_test_split

from base_conocimientos import intenciones
from clasificador_intenciones import entrenar_clasificador, evaluar_clasificador
from preprocesamiento_texto import preprocesar_texto
from representacion_texto import (
    crear_vectorizador,
    vectorizar_entrenamiento,
    vectorizar_textos,
)


def entrenar_y_evaluar_texto():
    textos = []
    etiquetas = []
    for intencion, datos in intenciones.items():
        for pregunta in datos["dudas"]:
            textos.append(preprocesar_texto(pregunta))
            etiquetas.append(intencion)

    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        textos, etiquetas, test_size=0.20, random_state=42, stratify=etiquetas,
    )

    vectorizador = crear_vectorizador()
    vectores_entrenamiento = vectorizar_entrenamiento(x_entrenamiento, vectorizador)
    vectores_prueba = vectorizar_textos(x_prueba, vectorizador)
    print(f"Preguntas: {len(textos)} | Intenciones: {len(set(etiquetas))}")
    print("Ejemplos por intención:", dict(Counter(etiquetas)))
    print("Textos procesados vacíos:", sum(not texto.strip() for texto in textos))
    print("Matriz de entrenamiento:", vectores_entrenamiento.shape)
    print("Matriz de prueba:", vectores_prueba.shape)

    modelo = entrenar_clasificador(vectores_entrenamiento, y_entrenamiento)
    evaluar_clasificador(modelo, vectores_prueba, y_prueba)


if __name__ == "__main__":
    entrenar_y_evaluar_texto()
