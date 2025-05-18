# Proyecto README Generator

Este proyecto tiene como objetivo principal generar un archivo README.md de manera automática a partir de la información proporcionada. Al ejecutar el script `main.py`, se pueden utilizar diferentes opciones para definir el contenido de salida y el archivo de destino.

## Uso

Para ejecutar el script y generar el README, se pueden utilizar las siguientes opciones:

- `-f prompt.txt`: Genera el contenido del README utilizando un archivo de texto como prompt.
- `-c "contenido del readme mal estructurado"`: Genera el contenido del README a partir de un texto proporcionado directamente en la terminal.
- `-o "../README.md"`: Define la ubicación y nombre del archivo de salida.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- `main.py`: Archivo principal que controla la generación del README.
- `services/`: Directorio que contiene los servicios relacionados con la generación del README.
  - `readme_generator.py`: Módulo encargado de generar el contenido del README.
- `api/`: Directorio que contiene los archivos relacionados con la API.
  - `openai_api.py`: Módulo que se encarga de interactuar con la API de OpenAI.

## Configuración

Para que el proyecto funcione correctamente, es necesario definir la API propia de OpenAI en un archivo `.env` o directamente en el código, según se prefiera.

## Información Adicional

Este proyecto utiliza la API de OpenAI para generar contenido de manera automatizada. La estructura del README generado sigue un formato definido, con el objetivo de ofrecer un resultado profesional y bien diseñado.

---

¡Gracias por utilizar el Proyecto README Generator! Esperamos que esta herramienta sea de utilidad para simplificar la creación de READMEs estructurados y profesionales.