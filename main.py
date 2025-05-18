import argparse
from services.readme_generator import generate_readme

def main():
    parser = argparse.ArgumentParser(description="Generador de README con OpenAI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Ruta al archivo con la descripción del proyecto")
    group.add_argument("-c", "--content", help="Descripción del proyecto directamente en línea")
    
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            description = f.read()
    else:
        description = args.content

    readme = generate_readme(description)

    with open("README.md", "w", encoding='utf-8') as f:
        f.write(readme)
    print("README.md generado exitosamente.")

if __name__ == "__main__":
    main()
