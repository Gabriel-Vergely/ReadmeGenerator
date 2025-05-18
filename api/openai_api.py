import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Usa la clave desde variable de entorno por seguridad
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_readme_from_openai(project_description: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un creador de README profesional. "
                "Cuando se te pase la descripción del proyecto, devolverás un README "
                "estructurado, definido, profesional y con buen diseño."
            )
        },
        {
            "role": "user",
            "content": f"Descripción del proyecto:\n\n{project_description}"
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
