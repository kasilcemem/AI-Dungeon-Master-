from utils.helpers import rand

CONNECTORS = [
    "Üstelik,", "Bunun yanında,", "Ve işte o an,", "Tam da bu sırada,",
]

class NarratorAgent:
    def run(self, world: str, story: str, enemy: dict, loot: dict, battle_result: str) -> str:
        connector = rand(CONNECTORS)
        lines = [
            f"🌍 {world}",
            f"",
            f"📖 {story}",
            f"",
            f"{connector} {enemy['emoji']} {enemy['name']} karşında!",
            f"",
            f"⚔️  {battle_result}",
        ]
        return "\n".join(lines)
