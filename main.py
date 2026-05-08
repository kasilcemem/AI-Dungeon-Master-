import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from agents.planner import WorldAgent
from agents.coder import StoryAgent
from agents.reviewer import EnemyAgent
from agents.executor import LootAgent
from utils.ollama_client import NarratorAgent
from game.player import Player
from game.combat import battle

LOCATIONS = [
    "Karanlık Orman", "Ejderha Mağarası", "Büyücü Kulesi",
    "Sisli Bataklık", "Antik Tapınak",
]

def run_parallel(action: str, player: Player) -> dict:
    print("\n  ⚡ Paralel ajanlar çalışıyor...")
    results = {}
    enemy_data = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(WorldAgent().run, player.location): "world",
            executor.submit(StoryAgent().run, action, player.location): "story",
            executor.submit(EnemyAgent().run, player.level): "enemy",
        }
        for future in as_completed(futures):
            key = futures[future]
            results[key] = future.result()
            print(f"  ✓ {key} ajanı tamamlandı")
            if key == "enemy":
                enemy_data = results[key]

    results["loot"] = LootAgent().run(enemy_data)
    print(f"  ✓ loot ajanı tamamlandı")
    return results

def main():
    print("\n" + "🐉" * 25)
    print("     AI DUNGEON MASTER")
    print("  Paralel Ajan RPG Sistemi")
    print("🐉" * 25)

    name = input("\nKahraman adın: ").strip() or "Kahraman"
    player = Player(name)
    narrator = NarratorAgent()

    print(f"\n⚔️  Hoş geldin, {player.name}! Macera başlıyor...")
    time.sleep(1)

    while player.hp > 0:
        player.status()
        action = input("\n🗡️  Ne yapıyorsun? ('q' çıkış, 'i' iksir): ").strip()
        if not action:
            continue
        if action.lower() == "q":
            print(f"\n👋 {player.name} efsane olarak tarihe geçti!")
            break
        if action.lower() == "i":
            if "🧪 Sağlık İksiri" in player.inventory:
                player.inventory.remove("🧪 Sağlık İksiri")
                player.heal(30)
                print(f"💊 İksir içtin! HP: {player.hp}")
            else:
                print("❌ Envanterinde iksir yok!")
            continue

        results = run_parallel(action, player)
        enemy = results["enemy"]
        battle_result, won = battle(player, enemy)
        scene = narrator.run(results["world"], results["story"], enemy, results["loot"], battle_result)

        print("\n" + "─" * 50)
        print(scene)

        if won:
            player.add_xp(enemy["xp"])
            player.gold += results["loot"]["gold"]
            player.inventory.append(results["loot"]["item"])
            player.kills += 1
            player.location = random.choice(LOCATIONS)
            print(f"\n{results['loot']['text']}")
            print(f"🪙 +{results['loot']['gold']} altın!")
        print("─" * 50)

        if player.hp <= 0:
            print(f"\n💀 {player.name} yenildi!")
            print(f"📊 Lv.{player.level} | {player.kills} düşman | {player.gold} altın")
            break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
