import pygame

from settings import *


class EnemyBullet:

    image = None

    width = 30
    height = 50

    def __init__(self, x, y):

        if EnemyBullet.image is None:

            EnemyBullet.image = pygame.image.load(
                "assets/images/enemy_bullet.png"
            )

            EnemyBullet.image = pygame.transform.smoothscale(
                EnemyBullet.image,
                (EnemyBullet.width, EnemyBullet.height)
            )

        self.x = x - self.width // 2
        self.y = y

        self.speed = ENEMY_BULLET_SPEED

    def update(self):

        self.y += self.speed

    def draw(self, screen):

        screen.blit(
            EnemyBullet.image,
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

        return self.y > HEIGHT