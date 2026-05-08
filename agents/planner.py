import random

DESCRIPTIONS = {
    "Karanlık Orman": [
        "Ağaçlar gökyüzünü kapatmış, ışık neredeyse yok.",
        "Sisli bir orman yolu seni bekliyor. Uzaktan kurt uluması geliyor.",
    ],
    "Ejderha Mağarası": [
        "Mağaranın duvarları kristallerle kaplı. Sıcaklık dayanılmaz.",
        "Yanmış kemikler yolunun her yanını kaplıyor.",
    ],
    "Büyücü Kulesi": [
        "Kitaplar havada uçuşuyor, mumlar kendiliğinden yanıyor.",
        "Büyülü semboller duvarlarda parlıyor.",
    ],
    "Sisli Bataklık": [
        "Her adımda ayakların bataklığa gömülüyor.",
        "Yoğun sis içinde bir şeylerin hareket ettiğini hissediyorsun.",
    ],
    "Antik Tapınak": [
        "Taş sütunlar asırlardır burada duruyor.",
        "Duvarlar eski bir uygarlığın resimlerini taşıyor.",
    ],
}
DEFAULT = ["Etraf sessiz ve tehlikeli.", "Yolun ilerisinde ne olduğunu bilmiyorsun."]

class WorldAgent:
    def run(self, location: str) -> str:
        return random.choice(DESCRIPTIONS.get(location, DEFAULT))
