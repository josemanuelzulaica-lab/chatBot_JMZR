#texto mediante TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer


def crear_vectorizador():
    return TfidfVectorizer(
        lowercase=False,
        token_pattern=r"(?u)\b\w+\b"
    )


def vectorizar_entrenamiento(textos, vectorizador):
    return vectorizador.fit_transform(textos)


def vectorizar_textos(textos, vectorizador):
    return vectorizador.transform(textos)
