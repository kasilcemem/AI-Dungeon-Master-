class NarratorAgent:
    def run(self, world: str, story: str, enemy: dict, loot: dict, battle_result: str) -> str:
        return (
            f"🌍 {world}\n\n"
            f"📖 {story}\n\n"
            f"⚔️  {battle_result}"
        )
