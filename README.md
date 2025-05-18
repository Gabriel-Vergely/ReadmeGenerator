# README Generator

Este proyecto consiste en un generador de README profesional a partir de una descripción de proyecto. Al ejecutar `main.py`, se pueden pasar diferentes argumentos para personalizar la generación del README.

## Instalación
1. Clonar este repositorio
2. Instalar las dependencias con `pip install -r requirements.txt`

## Uso
```bash
main.py -f prompt.txt
main.py -c "contenido del README mal estructurado"
main.py -o "../README.md"
main.py -m openai
main.py -m zephyr
```

## Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:
- `main.py`: Archivo principal para ejecutar el generador de README.
- `services/`: Carpeta que contiene los servicios del generador.
  - `readme_generator.py`: Archivo que se encarga de generar el README.
- `api/`: Carpeta que contiene los archivos relacionados con las APIs.
  - `openai_api.py`: Archivo para interactuar con la API de OpenAI.

## Configuración de la API
Para que el proyecto funcione correctamente, es necesario definir la API de OpenAI en un archivo `.env` con las siguientes variables:
```
OPENAI_API_KEY=your_api_key
```

## Resultado
Al ejecutar el generador de README con la descripción proporcionada, se obtendrá un README estructurado, definido, profesional y con buen diseño.

¡Gracias por utilizar nuestro README Generator!