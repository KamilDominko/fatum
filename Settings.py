class Settings:
    """Klasa przechowująca kluczowe dane dla działania programu."""

    def __init__(self):
        self.game_title = "Runner"
        self.screen_width = 800
        self.screen_height = 400
        self.fps = 60

        self.theme_color = (94, 129, 162)
        self.font_color = (111, 196, 169)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.player_health = 50
        self.hp_bar_width = 300
        self.hp_bar_height = 30

        self.damage = 10
