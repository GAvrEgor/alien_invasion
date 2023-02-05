class Settings():
    """класс для хранения всех настроек"""

    def __init__(self):
        "инициализирует настройки игры"
        # параметры экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        # настройки корабля
        # параметры снаряда
        self.bullet_width = 50
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10
        # 1 обозначает движение вправо а -1 влево
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
