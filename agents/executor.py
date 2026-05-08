import random

ITEMS = [
    "⚔️ Kılıç +1","🛡️ Demir Kalkan","🧪 Sağlık İksiri",
    "📖 Büyü Kitabı","💎 Ejderha Taşı","🪄 Sihirli Değnek",
    "🎯 Keskin Ok","🪙 50 Altın",
]

class LootAgent:
    def run(self, enemy: dict) -> dict:
        item = random.choice(ITEMS)
        gold = random.randint(5, 30)
        return {
            "item": item,
            "gold": gold,
            "text": f"{enemy.get('emoji','')} {enemy.get('name','Düşman')}'dan {item} düştü!",
        }
