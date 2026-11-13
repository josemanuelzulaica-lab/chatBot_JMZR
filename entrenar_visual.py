import json
from pathlib import Path

from tensorflow import keras

RAIZ = Path(__file__).resolve().parent
CATEGORIAS = ["otras", "pago_contactless", "tarjeta_fisica"]


def entrenar_modelo_visual():
    dataset = RAIZ / "dataset_cnn"
    parametros = dict(class_names=CATEGORIAS, image_size=(224, 224), batch_size=16)
    entrenamiento = keras.utils.image_dataset_from_directory(
        dataset / "entrenamiento", shuffle=True, seed=42, **parametros,
    )
    validacion = keras.utils.image_dataset_from_directory(
        dataset / "validacion", shuffle=False, **parametros,
    )

    base = keras.applications.EfficientNetB0(
        weights="imagenet", include_top=False, input_shape=(224, 224, 3),
    )
    base.trainable = False
    entrada = keras.Input(shape=(224, 224, 3))
    caracteristicas = base(entrada, training=False)
    promedio = keras.layers.GlobalAveragePooling2D()(caracteristicas)
    salida = keras.layers.Dense(len(CATEGORIAS), activation="softmax")(promedio)
    modelo = keras.Model(entrada, salida, name="clasificador_visual")

    modelo.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss=keras.losses.SparseCategoricalCrossentropy(),
        metrics=["accuracy"],
    )
    parada_temprana = keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=5, restore_best_weights=True,
    )
    modelo.fit(
        entrenamiento, validation_data=validacion, epochs=20,
        callbacks=[parada_temprana],
    )
    perdida, exactitud = modelo.evaluate(validacion, verbose=0)
    print(f"Exactitud de validación: {exactitud:.2%}")
    print(f"Pérdida de validación: {perdida:.4f}")

    carpeta = RAIZ / "modelo_visual_reentrenado"
    carpeta.mkdir(exist_ok=True)
    modelo.save(carpeta / "clasificador_visual.keras")
    (carpeta / "categorias.json").write_text(
        json.dumps(CATEGORIAS, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    print("Modelo reentrenado:", carpeta)


if __name__ == "__main__":
    entrenar_modelo_visual()
