import pygame
import random


class SpaceBackground:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # Load background image
        self.image = pygame.image.load(
            "assets/backgrounds/space.png"
        ).convert()

        # Scale to game resolution
        self.image = pygame.transform.smoothscale(
            self.image,
            (self.width, self.height)
        )

        # ============================
        # STAR PARTICLES
        # ============================

        self.stars = []

        for _ in range(80):

            self.stars.append({
                "x": random.randint(0, self.width),
                "y": random.randint(0, self.height),
                "speed": random.uniform(0.2, 0.8),
                "size": random.choice([1, 1, 1, 2]),
                "brightness": random.randint(100, 220)
            })

        # ============================
        # SHOOTING STAR
        # ============================

        self.shooting_star = None

        self.shooting_timer = random.randint(
            180,
            420
        )

    def update(self):

        # ============================
        # NORMAL STARS
        # ============================

        for star in self.stars:

            star["y"] += star["speed"]

            if star["y"] > self.height:

                star["y"] = 0

                star["x"] = random.randint(
                    0,
                    self.width
                )

        # ============================
        # SHOOTING STAR TIMER
        # ============================

        self.shooting_timer -= 1

        if (
            self.shooting_timer <= 0
            and self.shooting_star is None
        ):

            self.shooting_star = {
                "x": random.randint(
                    0,
                    self.width
                ),
                "y": random.randint(
                    50,
                    self.height // 2
                ),
                "speed": 12
            }

            self.shooting_timer = random.randint(
                300,
                600
            )

        # ============================
        # SHOOTING STAR MOVEMENT
        # ============================

        if self.shooting_star is not None:

            self.shooting_star["x"] += (
                self.shooting_star["speed"]
            )

            self.shooting_star["y"] += (
                self.shooting_star["speed"] * 0.5
            )

            if (
                self.shooting_star["x"] > self.width
                or self.shooting_star["y"] > self.height
            ):

                self.shooting_star = None

    def draw(self, screen):

        # ============================
        # BACKGROUND IMAGE
        # ============================

        screen.blit(
            self.image,
            (0, 0)
        )

        # ============================
        # STAR PARTICLES
        # ============================

        for star in self.stars:

            brightness = star["brightness"]

            pygame.draw.circle(
                screen,
                (
                    brightness,
                    brightness,
                    brightness
                ),
                (
                    int(star["x"]),
                    int(star["y"])
                ),
                star["size"]
            )

        # ============================
        # SHOOTING STAR
        # ============================

        if self.shooting_star is not None:

            x = int(
                self.shooting_star["x"]
            )

            y = int(
                self.shooting_star["y"]
            )

            pygame.draw.line(
                screen,
                (220, 240, 255),
                (x, y),
                (x - 35, y - 18),
                3
            )

            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (x, y),
                3
            )