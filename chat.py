from argparse import ArgumentParser
from pathlib import Path

from chat_multimodal import responder_consulta
from flujo_conversacional import iniciar_chatbot


def main():
    parser = ArgumentParser(description="Asistente de tarjetas de crédito.")
    parser.add_argument("--pregunta", help="Consulta que responderá el chatbot.")
    parser.add_argument("--imagen", type=Path, help="Imagen opcional para clasificar.")
    args = parser.parse_args()

    if args.imagen is not None and not args.pregunta:
        parser.error("--imagen requiere --pregunta.")
    if args.imagen is not None and not args.imagen.is_file():
        parser.error(f"No se encontró la imagen: {args.imagen}")

    if args.pregunta:
        print(responder_consulta(args.pregunta, args.imagen))
    else:
        iniciar_chatbot()


if __name__ == "__main__":
    main()
