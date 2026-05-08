from utils.helpers import rand

TEMPLATES = [
    lambda a, l: f"{l}'nda '{a}' yaparken aniden bir ses duyuyorsun. Kalbin hızlanıyor.",
    lambda a, l: f"'{a}' için adım attığında {l} titremeye başlıyor. Bir şeyler yanlış.",
    lambda a, l: f"{l}'nın derinliklerinde '{a}' ararken gözlerin bir hareketi yakalıyor.",
    lambda a, l: f"'{a}' kararı vermiştin ama {l} seni başka bir yöne çekiyor.",
    lambda a, l: f"{l}'nda her şey durdu. '{a}' artık bekleyebilir — önce bu tehditle uğraşmalısın.",
]

class StoryAgent:
    def run(self, action: str, location: str) -> str:
        template = rand(TEMPLATES)
        return template(action, location)
