import random
from utils.helpers import rand

DESCRIPTIONS = {
    "Karanlık Orman": [
        "Ağaçlar gökyüzünü kapatmış, ışık neredeyse yok. Yapraklar hışırdıyor.",
        "Sisli bir orman yolu seni bekliyor. Uzaktan kurt uluması geliyor.",
        "Dev meşe ağaçları arasında yolunu bulmaya çalışıyorsun.",
    ],
    "Ejderha Mağarası": [
        "Mağaranın duvarları parlak kristallerle kaplı. Sıcaklık dayanılmaz.",
        "Yanmış kemikler yolunun her yanını kaplıyor. Dikkatli ol.",
        "Uzaktan bir nefes sesi geliyor. Dev bir gölge duvarda beliriyor.",
    ],
    "Büyücü Kulesi": [
        "Kitaplar havada uçuşuyor, mumlar kendiliğinden yanıyor.",
        "Büyülü semboller duvarlarda parlıyor. Hava elektrik yüklü.",
        "Kristal küre masanın üzerinde dönerek seni izliyor.",
    ],
    "Sisli Bataklık": [
        "Her adımda ayakların bataklığa gömülüyor. Kurbağalar bağırıyor.",
        "Yoğun sis içinde bir şeylerin hareket ettiğini hissediyorsun.",
        "Bataklık gazları havada asılı. Nereye gittiğini bilmiyorsun.",
    ],
    "Antik Tapınak": [
        "Taş sütunlar asırlardır burada duruyor. Hava tarihin ağırlığıyla dolu.",
        "Duvarlar eski bir uygarlığın resimlerini taşıyor.",
        "Tapınağın ortasında gizemli bir ışık parlıyor.",
    ],
}

DEFAULT = [
    "Etraf sessiz ve tehlikeli görünüyor.",
    "Yolun ilerisinde ne olduğunu bilmiyorsun.",
    "Hava değişiyor, bir şeyler yaklaşıyor.",
]

class WorldAgent:
    def run(self, location: str) -> str:
        options = DESCRIPTIONS.get(location, DEFAULT)
        return rand(options)
