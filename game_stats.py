class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset()

        self.game_active = False

    def reset(self):
        self.ships_left = self.ai_settings.ship_limit
