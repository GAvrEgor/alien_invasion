import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """класс представляющий пришельца"""
    def __init__(self, ai_game):
        """инициализируем пришельца и задаем позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # загрузка изображения пришельца
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # пришельцы появляются вверху экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение позиции пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """true если находится у края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
