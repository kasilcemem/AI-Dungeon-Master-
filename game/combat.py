from utils.helpers import randint

def battle(player, enemy: dict) -> tuple[str, bool]:
    player_atk = randint(8, 20) + player.level * 3
    enemy_atk = enemy["atk"] + randint(0, 5)

    enemy["hp"] -= player_atk
    won = enemy["hp"] <= 0

    if won:
        result = f"{player.name} {player_atk} hasar verdi! {enemy['emoji']} {enemy['name']} yenildi! 🎉"
    else:
        player.take_damage(enemy_atk)
        result = (
            f"{player.name} {player_atk} hasar verdi! "
            f"{enemy['emoji']} {enemy['name']} HP: {enemy['hp']}\n"
            f"⚔️  {enemy['name']} {enemy_atk} hasar verdi! "
            f"Senin HP: {player.hp}"
        )
    return result, won
