from utils.ollama_client import ask_ollama

class LootAgent:
    def generate(self, enemy_name: str, location: str) -> str:
        return ask_ollama(
            prompt=f"Düşman: {enemy_name}, Konum: {location}",
            system=(
                "Sen bir RPG ödül tasarımcısısın. "
                "Bu düşmanı yendikten sonra oyuncunun bulacağı "
                "1-2 item veya ödülü belirle. Kısa ve Türkçe yaz."
            )
        )
