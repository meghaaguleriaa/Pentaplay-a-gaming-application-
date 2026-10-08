import pygame
import random
import math


class EnemyExplosion:

    def __init__(self, x, y, size=50):

        self.x = x
        self.y = y
        self.size = size*0.5

        self.time = 0
        self.duration = 450

        self.finished = False

        self.particles = []

        # Create sparks and debris
        for _ in range(28):

            angle = random.uniform(
                0,
                math.pi * 2
            )

            speed = random.uniform(
                1.5,
                5.5
            )

            self.particles.append({
                "x": 0,
                "y": 0,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "size": random.uniform(2, 5),
                "life": random.randint(250, 450),
                "max_life": 450,
                "type": random.choice(
                    ["spark", "debris"]
                )
            })

    def update(self):

        self.time += 16

        for particle in self.particles:

            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]

            particle["vy"] += 0.035

            particle["life"] -= 16

        if self.time >= self.duration:

            self.finished = True

    def draw(self, screen):

        progress = min(
            self.time / self.duration,
            1
        )

        # -------------------------------------------------
        # EXPLOSION FLASH
        # -------------------------------------------------

        if progress < 0.18:

            flash_progress = progress / 0.18

            radius = int(
                self.size
                * (0.25 + flash_progress * 0.75)
            )

            pygame.draw.circle(
                screen,
                (255, 255, 220),
                (int(self.x), int(self.y)),
                radius
            )

        # -------------------------------------------------
        # FIREBALL
        # -------------------------------------------------

        if progress < 0.65:

            fire_progress = progress / 0.65

            radius = int(
                self.size
                * (0.35 + fire_progress * 0.9)
            )

            # Outer fire
            pygame.draw.circle(
                screen,
                (255, 70, 20),
                (int(self.x), int(self.y)),
                radius
            )

            # Inner fire
            pygame.draw.circle(
                screen,
                (255, 150, 30),
                (int(self.x), int(self.y)),
                int(radius * 0.70)
            )

            # Hot center
            pygame.draw.circle(
                screen,
                (255, 240, 120),
                (int(self.x), int(self.y)),
                int(radius * 0.38)
            )

        # -------------------------------------------------
        # SMOKE
        # -------------------------------------------------

        if progress > 0.35:

            smoke_progress = (
                progress - 0.35
            ) / 0.65

            smoke_radius = int(
                self.size
                * (0.4 + smoke_progress * 0.8)
            )

            smoke_surface = pygame.Surface(
                (
                    smoke_radius * 3,
                    smoke_radius * 3
                ),
                pygame.SRCALPHA
            )

            alpha = int(
                110 * (1 - smoke_progress)
            )

            pygame.draw.circle(
                smoke_surface,
                (70, 70, 75, alpha),
                (
                    smoke_radius * 1.5,
                    smoke_radius * 1.5
                ),
                smoke_radius
            )

            screen.blit(
                smoke_surface,
                (
                    int(self.x - smoke_radius * 1.5),
                    int(
                        self.y
                        - smoke_radius * 1.5
                        - smoke_progress * 15
                    )
                )
            )

        # -------------------------------------------------
        # SPARKS / DEBRIS
        # -------------------------------------------------

        for particle in self.particles:

            if particle["life"] <= 0:
                continue

            alpha = int(
                255
                * (
                    particle["life"]
                    / particle["max_life"]
                )
            )

            px = int(
                self.x + particle["x"]
            )

            py = int(
                self.y + particle["y"]
            )

            if particle["type"] == "spark":

                length = particle["size"] * 2

                pygame.draw.line(
                    screen,
                    (255, 170, 40),
                    (px, py),
                    (
                        int(
                            px
                            - particle["vx"] * length
                        ),
                        int(
                            py
                            - particle["vy"] * length
                        )
                    ),
                    max(
                        1,
                        int(particle["size"])
                    )
                )

            else:

                surface = pygame.Surface(
                    (
                        int(particle["size"] * 3),
                        int(particle["size"] * 3)
                    ),
                    pygame.SRCALPHA
                )

                pygame.draw.rect(
                    surface,
                    (120, 120, 120, alpha),
                    surface.get_rect()
                )

                screen.blit(
                    surface,
                    (
                        px,
                        py
                    )
                )