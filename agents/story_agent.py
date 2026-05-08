from utils.ollama_client import ask_ollama

class StoryAgent:
    def advance(self, player_action: str, history: str) -> str:
        return ask_ollama(
            prompt=f"Geçmiş olaylar:\n{history}\n\nOyuncu şimdi ne yapıyor: {player_action}",
            system=(
                "Sen bir RPG hikaye yazarısın. "
                "Oyuncunun eylemine göre hikayeyi ilerlet. "
                "2-3 cümle, heyecanlı ve sürükleyici yaz. Türkçe."
            )
        )
