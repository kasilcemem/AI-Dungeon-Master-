import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from agents.world_agent import WorldAgent
from agents.story_agent import StoryAgent
from agents.enemy_agent import EnemyAgent
from agents.loot_agent import LootAgent
from agents.narrator_agent import NarratorAgent
from game.player import Player

def run_parallel_agents(player_action: str, player: Player) -> dict:
    world = WorldAgent()
    story = StoryAgent()
    enemy = EnemyAgent()
    loot = LootAgent()

    print("\n⚡ 4 ajan paralel çalışıyor...")

    results = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(world.build, player_action, player.location): "world",
            executor.submit(story.advance, player_action, "\n".join(player.history[-3:])):  "story",
            executor.submit(enemy.encounter, player.location, player.level): "enemy",
            executor.submit(loot.generate, "bilinmeyen düşman", player.location): "loot",
        }
        for future in as_completed(futures):
            key = futures[future]
            results[key] = future.result()
            print(f"  ✓ {key} ajanı tamamlandı")

    return results

def main():
    print("=" * 55)
    print("   🐉 AI DUNGEON MASTER — Paralel Ajan RPG")
    print("=" * 55)

    name = input("\nKahraman adın: ").strip() or "Kahraman"
    player = Player(name)

    print(f"\nHoş geldin, {player.name}! Macera başlıyor...")

    narrator = NarratorAgent()

    while player.hp > 0:
        player.status()
        action = input("\n⚔️  Ne yapıyorsun? (çıkış için 'q'): ").strip()

        if action.lower() == 'q':
            print("\n👋 Oyun bitti. Güle güle!")
            break
        if not action:
            continue

        # 4 ajan paralel çalışır
        results = run_parallel_agents(action, player)

        # Narrator hepsini birleştirir
        print("\n📖 Anlatıcı sahneyi oluşturuyor...")
        enemy_raw = results["enemy"].get("raw", "") if isinstance(results["enemy"], dict) else str(results["enemy"])
        scene = narrator.narrate(
            results["world"],
            results["story"],
            enemy_raw,
            results["loot"]
        )

        print("\n" + "─" * 55)
        print(scene)
        print("─" * 55)

        # Oyun mekaniği
        player.history.append(f"Oyuncu: {action}")
        player.take_damage(10)
        player.add_xp(25)

        if player.hp <= 0:
            print("\n💀 Yenildin! Oyun bitti.")
            break

if __name__ == "__main__":
    main()
