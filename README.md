# Proyecto README Automático

Este proyecto tiene como objetivo generar un README.md estructurado, definido, profesional y con buen diseño a partir de una descripción de proyecto dada.

## Ejecución

Para generar un README automáticamente, puedes utilizar los siguientes comandos:

- `main.py -f prompt.txt`: Genera un README basado en el contenido de `prompt.txt`.
- `main.py -c "contenido del readme mal estructurado"`: Genera un README corrigiendo la estructura del contenido proporcionado.

## Estructura de carpetas

El proyecto está organizado de la siguiente manera:

- `main.py`: Archivo principal para ejecutar la generación del README.
- `services/`: Carpeta que contiene los servicios del proyecto.
- `api/`: Carpeta que incluye los archivos relacionados con la API.
- `services/readme_generator.py`: Archivo que se encarga de generar el README.
- `api/openai_api.py`: Archivo que define la integración con la API de OpenAI.

## Configuración

Para que el proyecto funcione correctamente, se debe definir la API propia de OpenAI en un archivo `.env` o directamente en el código.

---
Este README fue generado automáticamente. ¡Gracias por utilizar nuestro servicio!