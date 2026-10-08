import pygame

from settings import *


class Enemy:

    def __init__(self, x, y, ship_type="enemyBlack3"):

        # =================================================
        # LOAD ENEMY IMAGE
        # =================================================

        self.image = pygame.image.load(
            f"assets/images/{ship_type}.png"
        ).convert_alpha()

        original_width = self.image.get_width()
        original_height = self.image.get_height()

        # =================================================
        # SCALE ENEMY
        # =================================================

        scale = ENEMY_WIDTH / original_width

        self.width = int(original_width * scale)
        self.height = int(original_height * scale)

        self.image = pygame.transform.scale(
            self.image,
            (
                self.width,
                self.height
            )
        )

        # =================================================
        # POSITION
        # =================================================

        self.x = x
        self.y = y

        # =================================================
        # SHIP TYPE
        # =================================================

        self.ship_type = ship_type

        # =================================================
        # GLOW COLORS
        # =================================================

        if "Black" in ship_type:

            self.glow_color = (
                90,
                190,
                255
            )

        elif "Blue" in ship_type:

            self.glow_color = (
                0,
                210,
                255
            )

        elif "Green" in ship_type:

            self.glow_color = (
                80,
                255,
                140
            )

        elif "Red" in ship_type:

            self.glow_color = (
                255,
                80,
                80
            )

        else:

            self.glow_color = (
                100,
                200,
                255
            )

        # =================================================
        # CREATE GLOW
        # =================================================

        self.glow = self.create_glow()

    # =====================================================
    # CREATE SCI-FI GLOW
    # =====================================================

    def create_glow(self):

        # Larger canvas around the ship
        glow_width = int(
            self.width * 1.16
        )

        glow_height = int(
            self.height * 1.16
        )

        glow = pygame.Surface(
            (
                glow_width,
                glow_height
            ),
            pygame.SRCALPHA
        )

        # Create mask from the actual ship
        mask = pygame.mask.from_surface(
            self.image
        )

        # =================================================
        # COLORED MASK
        # =================================================

        mask_surface = mask.to_surface(
            setcolor=(
                self.glow_color[0],
                self.glow_color[1],
                self.glow_color[2],
                110
            ),
            unsetcolor=(
                0,
                0,
                0,
                0
            )
        )

        # =================================================
        # OUTER GLOW
        # =================================================

        for offset in range(5, 0, -1):

            layer = mask_surface.copy()

            # Keep outer layers subtle
            layer.set_alpha(
                12 + (5 - offset) * 5
            )

            glow.blit(
                layer,
                (
                    8 + offset,
                    8
                )
            )

            glow.blit(
                layer,
                (
                    8 - offset,
                    8
                )
            )

            glow.blit(
                layer,
                (
                    8,
                    8 + offset
                )
            )

            glow.blit(
                layer,
                (
                    8,
                    8 - offset
                )
            )

        # =================================================
        # MAIN GLOW
        # =================================================

        main_glow = mask_surface.copy()

        main_glow.set_alpha(
            80
        )

        glow.blit(
            main_glow,
            (
                8,
                8
            )
        )

        return glow

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self, direction):

        self.x += direction

    # =====================================================
    # SHOOT
    # =====================================================

    def shoot(self):

        return (
            self.x + self.width // 2,
            self.y + self.height
        )

    # =====================================================
    # DRAW
    # =====================================================

    def draw(self, screen):

        # Draw glow behind the ship
        glow_x = (
            self.x
            - (self.glow.get_width() - self.width) // 2
        )

        glow_y = (
            self.y
            - (self.glow.get_height() - self.height) // 2
        )

        screen.blit(
            self.glow,
            (
                glow_x,
                glow_y
            )
        )

        # Draw actual ship on top
        screen.blit(
            self.image,
            (
                self.x,
                self.y
            )
        )

    # =====================================================
    # COLLISION RECT
    # =====================================================

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )