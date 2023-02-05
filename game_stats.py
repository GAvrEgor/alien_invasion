class GameStats():
    """отслеживание статистики"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.resets_stats()
        self.game_active = False
        self.high_score = 0

    def resets_stats(self):
        """инициализирует статистику в игре"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
