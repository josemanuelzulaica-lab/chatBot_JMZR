
# Aplica normalización, tokenización, eliminación de stopwords y stemming

from nltk.stem.snowball import SnowballStemmer
from interprete_intenciones import procesar_pregunta, palabras_comunes

stemmer = SnowballStemmer("spanish")

def preprocesar_texto(texto):

    palabras = procesar_pregunta(texto)

    palabras = [
        palabra for palabra in palabras
        if palabra not in palabras_comunes
    ]

    palabras = [
        stemmer.stem(palabra)
        for palabra in palabras
    ]

    return " ".join(palabras)
