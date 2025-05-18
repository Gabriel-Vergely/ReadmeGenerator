# README

---

## Descripción del Proyecto

El proyecto consiste en la ejecución de un script `main.py` el cual permite generar un README estructurado a partir de un archivo de texto o de un contenido definido directamente. Al ejecutar el script, se pueden pasar los siguientes parámetros:

- `-f "prompt.txt"` para indicar un archivo de texto con el contenido a utilizar.
- `-c "contenido del readme mal estructurado"` para definir el contenido directamente en la línea de comandos.
- Opcional: `-o "../README.md"` para especificar la ubicación del archivo de salida.
- Opcional: `-m "openai"` o `-m "zephyr"` para seleccionar el modelo a utilizar (por defecto se utiliza el modelo de OpenAI).

El script utiliza la API de OpenAI para generar el contenido del README. El contexto proporcionado a la API es:

"Eres un creador de README profesional. Cuando se te pase la descripción del proyecto, devolverás un README estructurado, definido, profesional y con buen diseño."

La estructura del proyecto es la siguiente:

```
project
│   main.py
│
└───services
│   │   readme_generator.py
│   
└───api
    │   openai_api.py
```

Para que el proyecto funcione correctamente, es necesario definir la API propia del modelo a utilizar en un archivo `.env` o directamente en el script.

El proyecto está bajo una licencia de uso libre y el autor es Gabriel Vergely Fernández.

---

## Instalación

Para instalar las dependencias del proyecto, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

---

## Uso

Para generar un README, ejecuta el script `main.py` con los parámetros adecuados:

```bash
python main.py -f "prompt.txt" -o "../README.md"
```

ó

```bash
python main.py -c "contenido del readme mal estructurado" -m "zephyr"
```

---

## Licencia

Este proyecto se encuentra bajo la Licencia MIT. Para más información, revisa el archivo [LICENSE](LICENSE).

---

## Autor

Gabriel Vergely Fernández

---