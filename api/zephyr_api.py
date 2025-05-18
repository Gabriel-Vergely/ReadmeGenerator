import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_readme_from_zephyr(prompt: str) -> str:
    HF_API_TOKEN = os.getenv("HF_API_TOKEN")
    if not HF_API_TOKEN:
        raise ValueError("HF_API_TOKEN no definido en .env")

    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    system_prompt = (
        "Eres un creador de readmes profesional. A partir de la descripción de un proyecto, "
        "devuelve un README estructurado, definido, profesional y con buen diseño."
    )

    chat_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{prompt}\n<|assistant|>"

    payload = {
        "inputs": chat_prompt,
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.7,
        },
        "options": {"wait_for_model": True}
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(f"Error de Hugging Face: {data['error']}")

    return data[0]["generated_text"].split("<|assistant|>")[-1].strip()
