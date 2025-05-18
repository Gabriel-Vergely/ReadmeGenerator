import argparse
from services.readme_generator import generate_readme

def main():
    parser = argparse.ArgumentParser(description="Generador de README usando OpenAI")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Archivo de texto con el prompt")
    group.add_argument("-c", "--content", help="Contenido del readme mal estructurado")

    parser.add_argument("-o", "--output", default="README.md", help="Ruta donde se guardará el README generado")

    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            content = f.read()
    else:
        content = args.content

    readme_text = generate_readme(content)

    with open(args.output, "w") as f:
        f.write(readme_text)
    print(f"README guardado en {args.output}")

if __name__ == "__main__":
    main()
