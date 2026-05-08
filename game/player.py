class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.inventory = []
        self.location = "Karanlık Orman"
        self.kills = 0

    def add_xp(self, amount: int):
        self.xp += amount
        needed = self.level * 100
        if self.xp >= needed:
            self.xp -= needed
            self.level += 1
            self.hp = min(self.hp + 20, self.max_hp)
            return True
        return False

    def take_damage(self, dmg: int):
        self.hp = max(0, self.hp - dmg)

    def heal(self, amount: int):
        self.hp = min(self.max_hp, self.hp + amount)

    def status(self):
        bar = "█" * (self.hp // 10) + "░" * (10 - self.hp // 10)
        print(f"\n{'='*50}")
        print(f"  👤 {self.name}  |  ⭐ Lv.{self.level}  |  ✨ XP: {self.xp}/{self.level*100}")
        print(f"  ❤️  [{bar}] {self.hp}/{self.max_hp}")
        print(f"  🪙 Altın: {self.gold}  |  💀 Öldürülen: {self.kills}")
        print(f"  📍 Konum: {self.location}")
        if self.inventory:
            print(f"  🎒 Envanter: {', '.join(self.inventory[-5:])}")
        print(f"{'='*50}")
