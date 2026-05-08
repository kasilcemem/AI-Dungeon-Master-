import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def ask_ollama(prompt: str, system: str = "") -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Ollama çalışmıyor! 'ollama serve' komutunu çalıştır.")

def run_parallel(tasks: dict) -> dict:
    """
    tasks = {"anahtar": (prompt, system), ...}
    Hepsini aynı anda çalıştırır, sonuçları döner.
    """
    results = {}
    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        futures = {
            executor.submit(ask_ollama, prompt, system): key
            for key, (prompt, system) in tasks.items()
        }
        for future in as_completed(futures):
            key = futures[future]
            try:
                results[key] = future.result()
            except Exception as e:
                results[key] = f"Hata: {e}"
    return results
