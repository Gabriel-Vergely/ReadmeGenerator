from api.openai_api import get_readme_from_openai

def generate_readme(description: str) -> str:
    prompt = (
        "Eres un creador de README. Cuando se te pase la descripción del proyecto, "
        "devolverás un README estructurado, definido, profesional y con buen diseño.\n\n"
        f"Descripción del proyecto:\n{description}\n\nREADME:"
    )
    return get_readme_from_openai(prompt)
