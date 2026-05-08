from utils.helpers import rand, randint

ITEMS = [
    "⚔️ Kılıç +1", "🛡️ Demir Kalkan", "🧪 Sağlık İksiri",
    "📖 Büyü Kitabı", "🏺 Altın Kupa", "🗺️ Gizem Haritası",
    "💎 Ejderha Taşı", "🪄 Sihirli Değnek", "👢 Hız Çizmeleri",
    "🎯 Keskin Ok", "🔮 Kristal Küre", "🪙 50 Altın",
]

TEMPLATES = [
    lambda e, i: f"{e['emoji']} {e['name']}'ı yendikten sonra {i} buluyorsun!",
    lambda e, i: f"{e['name']}'ın çantasında {i} var. Şansın varmış!",
    lambda e, i: f"Zafer! {e['name']} yere düştü ve {i} bıraktı.",
]

class LootAgent:
    def run(self, enemy: dict) -> dict:
        item = rand(ITEMS)
        text = rand(TEMPLATES)(enemy, item)
        gold = randint(5, 30) * enemy.get("xp", 10) // 10
        return {"item": item, "text": text, "gold": gold}
