import random

ENEMIES = [
    {"name":"Goblin",  "emoji":"👺","base_hp":30, "base_atk":8,  "xp":25},
    {"name":"Troll",   "emoji":"👾","base_hp":60, "base_atk":15, "xp":50},
    {"name":"Vampir",  "emoji":"🧛","base_hp":45, "base_atk":12, "xp":40},
    {"name":"Ejderha", "emoji":"🐉","base_hp":100,"base_atk":25, "xp":100},
    {"name":"Zombi",   "emoji":"🧟","base_hp":35, "base_atk":10, "xp":30},
    {"name":"Cadı",    "emoji":"🧙","base_hp":40, "base_atk":18, "xp":45},
]

class EnemyAgent:
    def run(self, player_level: int) -> dict:
        base = random.choice(ENEMIES)
        scale = 1 + (player_level - 1) * 0.2
        return {
            "name": base["name"], "emoji": base["emoji"],
            "hp": int(base["base_hp"] * scale),
            "atk": int(base["base_atk"] * scale),
            "xp": base["xp"],
        }
