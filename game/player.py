class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.location = "Karanlık Orman"
        self.history = []

    def add_xp(self, amount: int):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.level += 1
            self.xp = 0
            print(f"\n⭐ Seviye atladın! Seviye {self.level}")

    def take_damage(self, dmg: int):
        self.hp -= dmg
        print(f"💔 {dmg} hasar aldın! HP: {self.hp}")

    def status(self):
        print(f"\n👤 {self.name} | ❤️ HP:{self.hp} | ⭐ Lv:{self.level} | 📍 {self.location}")
        if self.inventory:
            print(f"🎒 Envanter: {', '.join(self.inventory)}")
