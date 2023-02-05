import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """класс для управления стрельбой корабля"""

    def __init__(self, ai_game):
        """создает обьект снарядов в текущей позиции"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # создание снаряда в позиции (0 0) и назначении позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # позиция снаряда
        self.y = float(self.rect.y)

    def update(self):
        """перемещает снаряд по таектории"""
        self.y -= self.settings.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ввыод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
