import pygame
import random
import math

from settings import *
from src.entities.bullet import Bullet


class Player:

    def __init__(self, audio=None):

        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 100

        self.speed = PLAYER_SPEED

        # -------------------------------------------------
        # PLAYER IMAGES
        # -------------------------------------------------

        self.image = pygame.image.load(
            "assets/images/playerShip1_blue.png"
        ).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image,
            (self.width, self.height)
        )

        # Destroyed ship image
        self.destroyed_image = pygame.image.load(
            "assets/images/playerShip1_destroyed.png"
        ).convert_alpha()

        self.destroyed_image = pygame.transform.smoothscale(
            self.destroyed_image,
            (self.width, self.height)
        )

        # Player destruction state
        self.destroyed = False

        self.bullets = []
        self.animation_time = 0

        # Audio manager
        self.audio = audio

        self.engine_particles = [
            self.create_particle()
            for _ in range(14)
        ]

        self.glow = self.create_glow()

    # -------------------------------------------------
    # PARTICLES
    # -------------------------------------------------

    def create_particle(self):

        return {
            "x": random.uniform(
                self.width * 0.35,
                self.width * 0.65
            ),
            "y": random.uniform(
                self.height * 0.70,
                self.height * 0.82
            ),
            "speed": random.uniform(1.5, 3.5),
            "size": random.uniform(1.5, 3.5),
            "life": random.uniform(0.4, 1.0)
        }

    # -------------------------------------------------
    # GLOW
    # -------------------------------------------------

    def create_glow(self):

        padding = 10

        glow = pygame.Surface(
            (
                self.width + padding * 2,
                self.height + padding * 2
            ),
            pygame.SRCALPHA
        )

        mask = pygame.mask.from_surface(self.image)

        shape = mask.to_surface(
            setcolor=(0, 200, 255, 70),
            unsetcolor=(0, 0, 0, 0)
        )

        glow.blit(shape, (padding, padding))

        outer = pygame.transform.smoothscale(
            shape,
            (self.width + 12, self.height + 12)
        )

        outer.set_alpha(30)

        glow.blit(
            outer,
            (padding - 6, padding - 6)
        )

        return glow

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    def update(self):

        # Don't move/update normal player systems
        # after destruction
        if self.destroyed:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(
            0,
            min(self.x, WIDTH - self.width)
        )

        self.animation_time += 0.12

        for particle in self.engine_particles:

            particle["y"] += particle["speed"]
            particle["life"] -= 0.025

            if (
                particle["life"] <= 0
                or particle["y"] > self.height
            ):
                particle.update(
                    self.create_particle()
                )

        for bullet in self.bullets:
            bullet.update()

        self.bullets = [
            bullet
            for bullet in self.bullets
            if not bullet.off_screen()
        ]

    # -------------------------------------------------
    # SHOOT
    # -------------------------------------------------

    def shoot(self):

        if self.destroyed:
            return

        self.bullets.append(
            Bullet(
                self.x + self.width // 2 - BULLET_WIDTH // 2,
                self.y
            )
        )

        # Play sound exactly when the bullet is fired
        if self.audio:
            self.audio.play("player_shoot")

    # -------------------------------------------------
    # ENGINE FLAMES
    # -------------------------------------------------

    def draw_engine_trails(self, screen):

        pulse = (
            math.sin(self.animation_time * 2.5) + 1
        ) / 2

        length = 18 + pulse * 10

        for engine_x in (
            self.x + self.width * 0.39,
            self.x + self.width * 0.61
        ):

            pygame.draw.polygon(
                screen,
                (0, 210, 255),
                [
                    (
                        int(engine_x),
                        int(self.y + self.height * 0.82)
                    ),
                    (
                        int(engine_x + 8),
                        int(self.y + self.height * 0.84)
                    ),
                    (
                        int(engine_x),
                        int(
                            self.y
                            + self.height * 0.82
                            + length
                        )
                    ),
                    (
                        int(engine_x - 8),
                        int(self.y + self.height * 0.84)
                    )
                ]
            )

            pygame.draw.polygon(
                screen,
                (220, 250, 255),
                [
                    (
                        int(engine_x),
                        int(self.y + self.height * 0.83)
                    ),
                    (
                        int(engine_x + 4),
                        int(self.y + self.height * 0.85)
                    ),
                    (
                        int(engine_x),
                        int(
                            self.y
                            + self.height * 0.82
                            + length * 0.75
                        )
                    ),
                    (
                        int(engine_x - 4),
                        int(self.y + self.height * 0.85)
                    )
                ]
            )

    # -------------------------------------------------
    # PARTICLES
    # -------------------------------------------------

    def draw_engine_particles(self, screen):

        for p in self.engine_particles:

            pygame.draw.circle(
                screen,
                (80, 220, 255),
                (
                    int(self.x + p["x"]),
                    int(
                        self.y
                        + p["y"]
                        + self.height * 0.18
                    )
                ),
                max(1, int(p["size"]))
            )

    # -------------------------------------------------
    # ENERGY CORE
    # -------------------------------------------------

    def draw_energy_core(self, screen):

        pulse = (
            math.sin(self.animation_time * 3) + 1
        ) / 2

        radius = int(3 + pulse * 2)

        x = int(self.x + self.width * 0.50)
        y = int(self.y + self.height * 0.32)

        glow = pygame.Surface(
            (radius * 8, radius * 8),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow,
            (0, 210, 255, 35),
            (radius * 4, radius * 4),
            radius * 4
        )

        screen.blit(
            glow,
            (x - radius * 4, y - radius * 4)
        )

        pygame.draw.circle(
            screen,
            (130, 240, 255),
            (x, y),
            radius
        )

    # -------------------------------------------------
    # DRAW
    # -------------------------------------------------

    def draw(self, screen):

        # -------------------------------------------------
        # DESTROYED SHIP
        # -------------------------------------------------

        if self.destroyed:

            screen.blit(
                self.destroyed_image,
                (self.x, self.y)
            )

            return

        # -------------------------------------------------
        # NORMAL SHIP
        # -------------------------------------------------

        self.draw_engine_trails(screen)
        self.draw_engine_particles(screen)

        screen.blit(
            self.glow,
            (self.x - 10, self.y - 10)
        )

        screen.blit(
            self.image,
            (self.x, self.y)
        )

        self.draw_energy_core(screen)

        for bullet in self.bullets:
            bullet.draw(screen)