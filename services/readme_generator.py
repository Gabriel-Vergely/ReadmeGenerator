from api.openai_api import get_readme_from_openai
from api.zephyr_api import get_readme_from_zephyr


def generate_readme(content: str, model: str = "openai") -> str:
    prompt = (
        "Eres un creador de readmes profesional. A partir de la descripción de un proyecto, "
        "devolverás un README estructurado, definido, profesional y con buen diseño.\n\n"
        f"Descripción del proyecto:\n{content}"
    )

    if model.lower() == "openai":
        return get_readme_from_openai(prompt)
    elif model.lower() == "zephyr":
        return get_readme_from_zephyr(prompt)
    else:
        raise ValueError(f"Modelo no soportado: {model}")
