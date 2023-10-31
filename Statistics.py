import json


class Statistics:
    """Klasa przechowująca dane statystyczne gracza."""

    def __init__(self):
        self.reset()

    def reset(self):
        """Tworzy domyślne zmienne klasy."""
        self.score = 0
        self.distance = 0
        self.bananas = 0
        self.hs = self.load_hs("SCORE")
        self.hd = self.load_hs("DISTANCE")
        self.hb = self.load_hs("BANANAS")

    def load_hs(self, type="SCORE"):
        """Wczytuje plik data.json z najwyższym wynikiem. Jeżeli taki
        istnieje zwraca trzy wartości kolejno: score, distance, bananas.
        Jeżeli taki nie istnieje, tworzy go z wartościami 0, 0, 0."""
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                for i in data:
                    if i == type:
                        return data[i]
        except FileNotFoundError:
            self.save_hs(0, 0, 0)

    def save_hs(self, score, distance, bananas):
        """Zapisuje najwyższy wynik do pliku data.json."""
        with open("data.json", "w") as f:
            text = {"SCORE": score,
                    "DISTANCE": distance,
                    "BANANAS": bananas}
            json.dump(text, f)
