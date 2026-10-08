import pygame


class Explosion:

    def __init__(self, x, y, size):

        self.frames = []

        for i in range(20):

            image = pygame.image.load(
                f"assets/animations/fire{i:02d}.png"
            ).convert_alpha()

            image = pygame.transform.scale(
                image,
                (
                    size,
                    size
                )
            )

            self.frames.append(image)

        self.x = x
        self.y = y
        self.frame = 0
        self.timer = 0
        self.speed = 1
        self.finished = False

    def update(self):

        self.timer += 1

        if self.timer >= self.speed:

            self.timer = 0
            self.frame += 1

            if self.frame >= len(self.frames):

                self.finished = True

    def draw(self, screen):

        if not self.finished:

            image = self.frames[self.frame]

            screen.blit(
                image,
                (
                    self.x - image.get_width() // 2,
                    self.y - image.get_height() // 2
                )
            )