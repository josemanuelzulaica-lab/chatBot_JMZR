# Módulo de clasificación de intenciones con Naive Bayes

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Crear y entrenar el clasificador
def entrenar_clasificador(X_entrenamiento, y_entrenamiento):

    modelo = MultinomialNB()
    modelo.fit(X_entrenamiento, y_entrenamiento)

    return modelo


# Evaluar el desempeño del clasificador
def evaluar_clasificador(modelo, X_prueba, y_prueba):

    # Obtener las predicciones
    predicciones = modelo.predict(X_prueba)

    # Calcular exactitud
    exactitud = accuracy_score(y_prueba, predicciones)

    # Mostrar resultados
    print("Exactitud (accuracy):", round(exactitud * 100, 2), "%")

    print("\nReporte de clasificación:")
    print(classification_report(
        y_prueba,
        predicciones,
        zero_division=0
    ))

    print("\nMatriz de confusión:")
    print(confusion_matrix(y_prueba, predicciones))

    return predicciones