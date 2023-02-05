import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """класс для управления кораблем"""
    def __init__(self, ai_game):
        super().__init__()
        """инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # каждый корабль появляется внизу экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # флаг перемещения
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновляем позицию корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor
        # обновление атрибута на rect  на основании self.x
        self.rect.x = self.x

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """рисует корабль в точке"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = self.x