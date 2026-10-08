import pygame

from settings import *


class Bullet:

    image = None

    width = 30
    height = 50

    def __init__(self, x, y):

        if Bullet.image is None:

            Bullet.image = pygame.image.load(
                "assets/images/player_bullet.png"
            )

            Bullet.image = pygame.transform.smoothscale(
                Bullet.image,
                (Bullet.width, Bullet.height)
            )

        self.x = x - self.width // 2
        self.y = y - self.height

        self.speed = BULLET_SPEED

    def update(self):

        self.y -= self.speed

    def draw(self, screen):

        screen.blit(
            Bullet.image,
            (self.x, self.y)
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def off_screen(self):

        return self.y < -self.height