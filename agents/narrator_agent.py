from utils.ollama_client import ask_ollama

class NarratorAgent:
    def narrate(self, world: str, story: str, enemy: str, loot: str) -> str:
        combined = f"""
Dünya: {world}
Hikaye: {story}
Düşman: {enemy}
Ödül: {loot}
"""
        return ask_ollama(
            prompt=combined,
            system=(
                "Sen bir RPG anlatıcısısın. "
                "Verilen tüm bilgileri birleştirip oyuncuya "
                "akıcı, heyecanlı 4-5 cümlelik bir sahne sun. "
                "Türkçe yaz. Son cümle oyuncuya ne yapacağını sor."
            )
        )
