from utils.ollama_client import ask_ollama

class WorldAgent:
    def build(self, player_action: str, location: str) -> str:
        return ask_ollama(
            prompt=f"Konum: {location}\nOyuncu eylemi: {player_action}",
            system=(
                "Sen bir RPG dünya tasarımcısısın. "
                "Ortamı, mekanı, atmosferi 2-3 cümleyle Türkçe anlat. "
                "Sadece ortam tanımı yap, başka bir şey yazma."
            )
        )
