from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
)
from tensorflow import keras

from clasificador_visual import cargar_clasificador_visual

RAIZ = Path(__file__).resolve().parent


def evaluar_modelo_visual(carpeta_modelo=None):
    modelo, categorias = cargar_clasificador_visual(carpeta_modelo)
    prueba = keras.utils.image_dataset_from_directory(
        RAIZ / "dataset_cnn" / "prueba",
        class_names=categorias,
        image_size=(224, 224),
        batch_size=16,
        shuffle=False,
    )
    y_real = np.concatenate([etiquetas.numpy() for _, etiquetas in prueba])
    y_pred = modelo.predict(prueba, verbose=0).argmax(axis=1)
    etiquetas = list(range(len(categorias)))

    print(f"Exactitud (accuracy): {accuracy_score(y_real, y_pred):.2%}")
    print(f"Aciertos: {(y_real == y_pred).sum()} de {len(y_real)} imágenes")
    print(classification_report(
        y_real, y_pred, labels=etiquetas, target_names=categorias,
        digits=3, zero_division=0,
    ))

    fig, ax = plt.subplots(figsize=(7, 5))
    ConfusionMatrixDisplay.from_predictions(
        y_real, y_pred, labels=etiquetas, display_labels=categorias,
        cmap="Blues", values_format="d", xticks_rotation=25, ax=ax,
    )
    ax.set_title("Matriz de confusión — imágenes de prueba")
    ax.set_xlabel("Categoría predicha")
    ax.set_ylabel("Categoría real")
    fig.tight_layout()

    ruta = RAIZ / "matriz_confusion_visual.png"
    fig.savefig(ruta, dpi=150)
    plt.close(fig)
    print("Matriz guardada:", ruta)
    return ruta


if __name__ == "__main__":
    parser = ArgumentParser(description="Evalúa el modelo con las imágenes de prueba.")
    parser.add_argument("--modelo", type=Path, help="Carpeta con el modelo y su JSON.")
    args = parser.parse_args()
    evaluar_modelo_visual(args.modelo)
