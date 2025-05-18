import argparse
import os
from dotenv import load_dotenv
from services.readme_generator import generate_readme

def main():
    load_dotenv()  # Carga variables de entorno desde .env

    parser = argparse.ArgumentParser(description="Generador de README usando OpenAI o Mistral")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Archivo de texto con el prompt")
    group.add_argument("-c", "--content", help="Contenido del README mal estructurado")

    parser.add_argument("-o", "--output", default="README.md", help="Ruta donde se guardará el README generado")
    parser.add_argument("-m", "--model", default="openai", choices=["openai", "zephyr"], help="Modelo a utilizar: openai o zephyr")

    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            content = f.read()
    else:
        content = args.content

    readme = generate_readme(content, model=args.model)

    with open(args.output, "w") as f:
        f.write(readme)
    print(f"\n✅ README generado y guardado en: {args.output}")

if __name__ == "__main__":
    main()
