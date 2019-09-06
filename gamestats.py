class GameStats():
    """Отслеживание статистики для игры Alien invasion"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуеся в начале игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

        #Рекорд не должен сбрасываться




