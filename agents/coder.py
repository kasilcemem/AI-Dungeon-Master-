import random

TEMPLATES = [
    lambda a, l: f"{l}'nda '{a}' yaparken aniden bir ses duyuyorsun.",
    lambda a, l: f"'{a}' için adım attığında {l} titremeye başlıyor.",
    lambda a, l: f"{l}'nın derinliklerinde '{a}' ararken bir hareket yakalıyorsun.",
    lambda a, l: f"'{a}' kararı vermiştin ama {l} seni başka yöne çekiyor.",
]

class StoryAgent:
    def run(self, action: str, location: str) -> str:
        return random.choice(TEMPLATES)(action, location)
