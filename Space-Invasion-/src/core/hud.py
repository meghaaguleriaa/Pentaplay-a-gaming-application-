import pygame


class HUD:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # ==========================================
        # HUD PANEL
        # ==========================================

        self.hud_width = 270
        self.hud_height = 220

        self.hud_x = 18
        self.hud_y = 18

        # ==========================================
        # FONTS
        # ==========================================

        self.header_font = pygame.font.SysFont(
            "Arial",
            20,
            bold=True
        )

        self.label_font = pygame.font.SysFont(
            "Arial",
            15,
            bold=True
        )

        self.score_font = pygame.font.SysFont(
            "Arial",
            34,
            bold=True
        )

        self.wave_font = pygame.font.SysFont(
            "Arial",
            34,
            bold=True
        )

        self.status_font = pygame.font.SysFont(
            "Arial",
            14,
            bold=True
        )

    # ==============================================
    # DRAW HUD
    # ==============================================

    def draw(
        self,
        screen,
        score,
        lives,
        wave,
        game_over,
        wave_transition
    ):

        # ==========================================
        # CREATE TRANSPARENT PANEL
        # ==========================================

        hud = pygame.Surface(
            (
                self.hud_width,
                self.hud_height
            ),
            pygame.SRCALPHA
        )

        # ==========================================
        # MAIN GLASS PANEL
        # ==========================================

        pygame.draw.rect(
            hud,
            (5, 10, 25, 205),
            (
                0,
                0,
                self.hud_width,
                self.hud_height
            ),
            border_radius=14
        )

        # ==========================================
        # OUTER BORDER
        # ==========================================

        pygame.draw.rect(
            hud,
            (80, 150, 220, 220),
            (
                0,
                0,
                self.hud_width,
                self.hud_height
            ),
            width=2,
            border_radius=14
        )

        # ==========================================
        # INNER BORDER
        # ==========================================

        pygame.draw.rect(
            hud,
            (40, 80, 130, 120),
            (
                6,
                6,
                self.hud_width - 12,
                self.hud_height - 12
            ),
            width=1,
            border_radius=10
        )

        # ==========================================
        # HEADER
        # ==========================================

        header = self.header_font.render(
            "◈  MISSION CONTROL",
            True,
            (180, 220, 255)
        )

        hud.blit(
            header,
            (18, 12)
        )

        # ==========================================
        # HEADER LINE
        # ==========================================

        pygame.draw.line(
            hud,
            (70, 130, 190, 160),
            (18, 42),
            (self.hud_width - 18, 42),
            1
        )

        # ==========================================
        # SCORE LABEL
        # ==========================================

        score_label = self.label_font.render(
            "SCORE",
            True,
            (130, 160, 190)
        )

        hud.blit(
            score_label,
            (18, 55)
        )

        # ==========================================
        # SCORE
        # ==========================================

        score_text = self.score_font.render(
            f"{score:05d}",
            True,
            (255, 255, 255)
        )

        hud.blit(
            score_text,
            (18, 72)
        )

        # ==========================================
        # WAVE LABEL
        # ==========================================

        wave_label = self.label_font.render(
            "WAVE",
            True,
            (130, 160, 190)
        )

        hud.blit(
            wave_label,
            (165, 55)
        )

        # ==========================================
        # WAVE NUMBER
        # ==========================================

        wave_text = self.wave_font.render(
            f"{wave:02d}",
            True,
            (180, 220, 255)
        )

        hud.blit(
            wave_text,
            (165, 72)
        )

        # ==========================================
        # DIVIDER
        # ==========================================

        pygame.draw.line(
            hud,
            (70, 130, 190, 130),
            (18, 116),
            (self.hud_width - 18, 116),
            1
        )

        # ==========================================
        # HULL LABEL
        # ==========================================

        hull_label = self.label_font.render(
            "SHIP'S HEALTH",
            True,
            (130, 160, 190)
        )

        hud.blit(
            hull_label,
            (18, 130)
        )

        # ==========================================
        # HULL BARS
        # ==========================================

        for i in range(3):

            x = 20 + i * 45
            y = 157

            # Empty bar
            pygame.draw.rect(
                hud,
                (35, 45, 60),
                (
                    x,
                    y,
                    35,
                    15
                ),
                border_radius=4
            )

            # Active bar
            if i < lives:

                pygame.draw.rect(
                    hud,
                    (50, 190, 240),
                    (
                        x,
                        y,
                        35,
                        15
                    ),
                    border_radius=4
                )

                # Highlight
                pygame.draw.rect(
                    hud,
                    (150, 230, 255),
                    (
                        x + 3,
                        y + 3,
                        29,
                        3
                    ),
                    border_radius=2
                )

        # ==========================================
        # SYSTEM STATUS
        # ==========================================

        if game_over:

            status_text = "● SYSTEM OFFLINE"
            status_color = (255, 80, 80)

        elif wave_transition:

            status_text = "● WAVE INITIALIZING"
            status_color = (255, 210, 80)

        else:

            status_text = "● SYSTEM ONLINE"
            status_color = (100, 255, 170)

        status = self.status_font.render(
            status_text,
            True,
            status_color
        )

        hud.blit(
            status,
            (18, 190)
        )

        # ==========================================
        # DECORATIVE CIRCUITS
        # ==========================================

        pygame.draw.line(
            hud,
            (70, 130, 190, 120),
            (170, 190),
            (215, 190),
            1
        )

        pygame.draw.line(
            hud,
            (70, 130, 190, 120),
            (225, 190),
            (250, 190),
            1
        )

        pygame.draw.circle(
            hud,
            (80, 160, 220, 180),
            (260, 190),
            3
        )

        # ==========================================
        # DRAW HUD ON SCREEN
        # ==========================================

        screen.blit(
            hud,
            (
                self.hud_x,
                self.hud_y
            )
        )