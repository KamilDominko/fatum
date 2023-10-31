class Statistics:
    """Klasa przechowująca dane statystyczne gracza."""

    def __init__(self):
        self.score = 0
        self.distance = 0
        self.bananas = 0

    def reset(self):
        self.score = 0
        self.distance = 0
        self.bananas = 0
