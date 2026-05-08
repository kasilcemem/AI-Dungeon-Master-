from utils.ollama_client import ask_ollama
import random

class EnemyAgent:
    def encounter(self, location: str, player_level: int) -> dict:
        response = ask_ollama(
            prompt=f"Konum: {location}, Oyuncu seviyesi: {player_level}",
            system=(
                "Sen bir RPG düşman tasarımcısısın. "
                "Bu konuma uygun bir düşman oluştur. "
                "Sadece şu formatta yaz:\n"
                "İsim: ...\nHP: ...\nGüç: ...\nTanım: ..."
            )
        )
        enemy = {"raw": response, "hp": random.randint(20, 50) + player_level * 5}
        return enemy
