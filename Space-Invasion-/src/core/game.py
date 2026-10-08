import pygame
import random
import math

from settings import *

from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.enemy_bullet import EnemyBullet

from src.core.background import SpaceBackground
from src.core.hud import HUD
from src.core.audio import Audio

from src.core.formation import (
    create_grid,
    create_triangle,
    create_diamond,
    create_v,
    create_cross,
    create_arrow,
    create_hollow_rectangle,
    SHIP_TYPES
)

from src.core.difficulty import (
    get_enemy_speed,
    get_shoot_interval,
    get_max_shooters
)

# ENEMY EXPLOSION

class EnemyExplosion:

    def __init__(self, x, y, size=50):

        self.x = x
        self.y = y
        self.size = size

        self.age = 0
        self.duration = 500

        self.finished = False

        self.particles = []

        # Create sparks and debris
        for _ in range(32):

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
                "life": random.randint(250, 500),
                "max_life": 500,
                "type": random.choice(
                    ["spark", "debris"]
                )
            })

    def update(self):

        self.age += 16

        for particle in self.particles:

            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]

            # Slight gravity
            particle["vy"] += 0.035

            particle["life"] -= 16

        if self.age >= self.duration:

            self.finished = True

    def draw(self, screen):

        progress = min(
            self.age / self.duration,
            1
        )

        center = (
            int(self.x),
            int(self.y)
        )

        # INITIAL FLASH

        if progress < 0.16:

            flash_progress = (
                progress / 0.16
            )

            radius = int(
                self.size
                * (
                    0.15
                    + flash_progress * 0.45
                )
            )

            pygame.draw.circle(
                screen,
                (255, 255, 230),
                center,
                radius
            )

        # FIREBALL

        if progress < 0.65:

            fire_progress = (
                progress / 0.65
            )

            radius = int(
                self.size
                * (
                    0.25
                    + fire_progress * 0.85
                )
            )

            # Outer red/orange fire
            pygame.draw.circle(
                screen,
                (230, 45, 10),
                center,
                radius
            )

            # Main orange fire
            pygame.draw.circle(
                screen,
                (255, 100, 15),
                center,
                int(radius * 0.82)
            )

            # Yellow hot area
            pygame.draw.circle(
                screen,
                (255, 185, 35),
                center,
                int(radius * 0.58)
            )

            # White-hot center
            pygame.draw.circle(
                screen,
                (255, 240, 150),
                center,
                int(radius * 0.28)
            )

        # SMOKE

        if progress > 0.25:

            smoke_progress = (
                progress - 0.25
            ) / 0.75

            smoke_progress = max(
                0,
                min(smoke_progress, 1)
            )

            smoke_radius = int(
                self.size
                * (
                    0.35
                    + smoke_progress * 0.75
                )
            )

            smoke_surface = pygame.Surface(
                (
                    smoke_radius * 3,
                    smoke_radius * 3
                ),
                pygame.SRCALPHA
            )

            alpha = int(
                120
                * (1 - smoke_progress)
            )

            # Several overlapping smoke blobs
            smoke_positions = [
                (
                    smoke_radius * 1.5,
                    smoke_radius * 1.5
                ),
                (
                    smoke_radius * 1.1,
                    smoke_radius * 1.35
                ),
                (
                    smoke_radius * 1.9,
                    smoke_radius * 1.3
                ),
                (
                    smoke_radius * 1.5,
                    smoke_radius * 1.05
                )
            ]

            for sx, sy in smoke_positions:

                pygame.draw.circle(
                    smoke_surface,
                    (55, 55, 60, alpha),
                    (
                        int(sx),
                        int(sy)
                    ),
                    int(smoke_radius * 0.55)
                )

            screen.blit(
                smoke_surface,
                (
                    int(
                        self.x
                        - smoke_radius * 1.5
                    ),
                    int(
                        self.y
                        - smoke_radius * 1.5
                        - smoke_progress * 18
                    )
                )
            )

        # SPARKS + DEBRIS

        for particle in self.particles:

            if particle["life"] <= 0:
                continue

            life_ratio = (
                particle["life"]
                / particle["max_life"]
            )

            px = int(
                self.x + particle["x"]
            )

            py = int(
                self.y + particle["y"]
            )

            # ---------------------------------------------
            # SPARK
            # ---------------------------------------------

            if particle["type"] == "spark":

                length = (
                    particle["size"] * 2.5
                )

                pygame.draw.line(
                    screen,
                    (255, 170, 35),
                    (px, py),
                    (
                        int(
                            px
                            - particle["vx"]
                            * length
                        ),
                        int(
                            py
                            - particle["vy"]
                            * length
                        )
                    ),
                    max(
                        1,
                        int(
                            particle["size"]
                        )
                    )
                )

            # ---------------------------------------------
            # DEBRIS
            # ---------------------------------------------

            else:

                debris_size = max(
                    2,
                    int(
                        particle["size"]
                        * life_ratio
                    )
                )

                pygame.draw.rect(
                    screen,
                    (100, 100, 105),
                    (
                        px,
                        py,
                        debris_size,
                        debris_size
                    )
                )

class Game:

    def __init__(self):

        pygame.init()

        # AUDIO

        self.audio = Audio()
        self.audio.play_music()

        # WINDOW

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT),
            pygame.RESIZABLE | pygame.SCALED
        )

        pygame.display.set_caption(TITLE)

        # Start maximized while keeping
        # the normal Windows title bar
        try:
            window = pygame._sdl2.Window.from_display_module()
            window.maximize()
        except:
            pass

        self.clock = pygame.time.Clock()

        # FONTS

        self.font = pygame.font.SysFont(
            "Arial",
            32
        )

        self.big_font = pygame.font.SysFont(
            "Arial",
            64
        )

        self.small_font = pygame.font.SysFont(
            "Arial",
            24
        )

        # BACKGROUND

        self.background = SpaceBackground(
            WIDTH,
            HEIGHT
        )

        # HUD

        self.hud = HUD(
            WIDTH,
            HEIGHT
        )

        # GAME SETTINGS

        self.enemy_speed = get_enemy_speed(1)

        self.enemy_drop = 40

        self.score = 0
        self.lives = 3
        self.wave = 1

        self.game_over = False
        self.start_screen = True

        # BULLETS / EFFECTS

        self.enemy_bullets = []
        self.explosions = []

        # PLAYER / ENEMIES

        self.enemies = create_grid(
            "enemyBlack3"
        )

        self.player = Player(self.audio)

        # ENEMY SHOOTING TIMER

        self.ENEMY_SHOOT_EVENT = pygame.USEREVENT + 1

        pygame.time.set_timer(
            self.ENEMY_SHOOT_EVENT,
            get_shoot_interval(self.wave)
        )

        # WAVE TRANSITION

        self.wave_transition = True

        self.wave_transition_time = 2000

        self.wave_start_time = pygame.time.get_ticks()

        # GAME LOOP

        # Menu ship textures
        self.menu_player_image = None
        self.menu_enemy_image = None

        try:
            self.menu_player_image = pygame.image.load(
                "assets/images/playerShip1_blue.png"
            ).convert_alpha()
            self.menu_enemy_image = pygame.image.load(
                "assets/images/enemyBlack3.png"
            ).convert_alpha()

            self.menu_player_image = pygame.transform.smoothscale(
                self.menu_player_image,
                (90, 90)
            )
            self.menu_enemy_image = pygame.transform.smoothscale(
                self.menu_enemy_image,
                (75, 75)
            )
        except (pygame.error, FileNotFoundError):
            pass

        self.running = True

    # START SCREEN

    def start_game(self):

        self.start_screen = False
        self.reset_game()

    def draw_start_screen(self):

        # Use the exact same animated space background as gameplay.
        self.background.draw(self.screen)

        center_x = WIDTH // 2
        mouse_pos = pygame.mouse.get_pos()

        # -------------------------------------------------
        # DARK SCI-FI OVERLAY
        # -------------------------------------------------

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 95))
        self.screen.blit(overlay, (0, 0))

        # Subtle sci-fi grid texture
        grid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        grid_spacing = 45

        for x in range(0, WIDTH, grid_spacing):
            pygame.draw.line(
                grid_surface,
                (70, 150, 190, 28),
                (x, 0),
                (x, HEIGHT),
                1
            )

        for y in range(0, HEIGHT, grid_spacing):
            pygame.draw.line(
                grid_surface,
                (70, 150, 190, 28),
                (0, y),
                (WIDTH, y),
                1
            )

        self.screen.blit(grid_surface, (0, 0))

        # -------------------------------------------------
        # SIDE SHIP TEXTURES
        # -------------------------------------------------

        if self.menu_player_image:
            player_rect = self.menu_player_image.get_rect(
                center=(center_x - 390, HEIGHT // 2 + 20)
            )
            self.screen.blit(self.menu_player_image, player_rect)

        if self.menu_enemy_image:
            enemy_rect = self.menu_enemy_image.get_rect(
                center=(center_x + 390, HEIGHT // 2 - 20)
            )
            self.screen.blit(self.menu_enemy_image, enemy_rect)

        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        title_shadow = self.big_font.render(
            "SPACE INVASION", True, (0, 20, 30)
        )
        title = self.big_font.render(
            "SPACE INVASION", True, (180, 235, 255)
        )

        title_pos = (
            center_x - title.get_width() // 2,
            HEIGHT // 2 - 190
        )

        self.screen.blit(
            title_shadow,
            (title_pos[0] + 4, title_pos[1] + 5)
        )
        self.screen.blit(title, title_pos)

        # Decorative lines under the title
        line_y = HEIGHT // 2 - 112
        pygame.draw.line(
            self.screen,
            (80, 190, 230),
            (center_x - 230, line_y),
            (center_x - 45, line_y),
            2
        )
        pygame.draw.line(
            self.screen,
            (80, 190, 230),
            (center_x + 45, line_y),
            (center_x + 230, line_y),
            2
        )

        status = self.small_font.render(
            "MISSION CONTROL",
            True,
            (110, 190, 215)
        )

        self.screen.blit(
            status,
            (
                center_x - status.get_width() // 2,
                HEIGHT // 2 - 92
            )
        )

        # -------------------------------------------------
        # BUTTONS
        # -------------------------------------------------

        start_button = pygame.Rect(
            center_x - 155,
            HEIGHT // 2 - 45,
            310,
            62
        )

        quit_button = pygame.Rect(
            center_x - 155,
            HEIGHT // 2 + 35,
            310,
            62
        )

        start_hover = start_button.collidepoint(mouse_pos)
        quit_hover = quit_button.collidepoint(mouse_pos)

        # Dark translucent panels
        start_panel = pygame.Surface(
            start_button.size, pygame.SRCALPHA
        )
        quit_panel = pygame.Surface(
            quit_button.size, pygame.SRCALPHA
        )

        start_panel.fill(
            (20, 100, 135, 210 if start_hover else 165)
        )
        quit_panel.fill(
            (45, 55, 65, 210 if quit_hover else 165)
        )

        self.screen.blit(start_panel, start_button.topleft)
        self.screen.blit(quit_panel, quit_button.topleft)

        pygame.draw.rect(
            self.screen,
            (90, 210, 245),
            start_button,
            2,
            border_radius=5
        )

        pygame.draw.rect(
            self.screen,
            (120, 135, 145),
            quit_button,
            2,
            border_radius=5
        )

        start_text = self.font.render(
            "START GAME", True, WHITE
        )
        quit_text = self.font.render(
            "QUIT", True, (220, 225, 230)
        )

        self.screen.blit(
            start_text,
            (
                start_button.centerx - start_text.get_width() // 2,
                start_button.centery - start_text.get_height() // 2
            )
        )

        self.screen.blit(
            quit_text,
            (
                quit_button.centerx - quit_text.get_width() // 2,
                quit_button.centery - quit_text.get_height() // 2
            )
        )

        # -------------------------------------------------
        # CONTROLS / FOOTER
        # -------------------------------------------------

        controls = self.small_font.render(
            "ENTER / SPACE  •  START        ESC  •  QUIT",
            True,
            (155, 180, 195)
        )

        self.screen.blit(
            controls,
            (
                center_x - controls.get_width() // 2,
                HEIGHT - 55
            )
        )

        version = self.small_font.render(
            "SPACE INVASION  •  SYSTEM READY",
            True,
            (75, 120, 135)
        )

        self.screen.blit(
            version,
            (
                25,
                HEIGHT - 35
            )
        )

        pygame.display.flip()

    # RESET GAME

    def reset_game(self):

        self.player = Player(self.audio)

        self.wave = 1

        self.enemies = create_grid(
            "enemyBlack3"
        )

        self.enemy_speed = get_enemy_speed(1)

        self.score = 0
        self.lives = 3

        self.enemy_bullets = []
        self.explosions = []

        self.game_over = False

        pygame.time.set_timer(
            self.ENEMY_SHOOT_EVENT,
            get_shoot_interval(self.wave)
        )

        self.wave_transition = True

        self.wave_start_time = pygame.time.get_ticks()

    # CREATE WAVE

    def create_wave(self):

        # -----------------------------
        # WAVE 1
        # -----------------------------

        if self.wave == 1:

            return create_grid(
                "enemyBlack3"
            )

        # -----------------------------
        # WAVE 2
        # -----------------------------

        if self.wave == 2:

            return create_triangle(
                "enemyBlue3"
            )

        # -----------------------------
        # WAVE 3
        # -----------------------------

        if self.wave == 3:

            return create_diamond(
                "enemyGreen3"
            )

        # -----------------------------
        # WAVE 4
        # -----------------------------

        if self.wave == 4:

            return create_v(
                "enemyRed3"
            )

        # -----------------------------
        # WAVE 5+
        # -----------------------------

        formations = [
            create_cross,
            create_arrow,
            create_hollow_rectangle
        ]

        formation = formations[
            (self.wave - 5) % len(formations)
        ]

        return formation(
            SHIP_TYPES
        )

    # HANDLE EVENTS

    def handle_events(self):

        for event in pygame.event.get():

            # -----------------------------
            # WINDOW CLOSE
            # -----------------------------

            if event.type == pygame.QUIT:

                self.running = False
                continue

            # -----------------------------
            # START SCREEN
            # -----------------------------

            if self.start_screen:

                if event.type == pygame.KEYDOWN:

                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):

                        self.start_game()

                    elif event.key == pygame.K_ESCAPE:

                        self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        start_button = pygame.Rect(
                            WIDTH // 2 - 140,
                            HEIGHT // 2 - 10,
                            280,
                            65
                        )

                        quit_button = pygame.Rect(
                            WIDTH // 2 - 140,
                            HEIGHT // 2 + 80,
                            280,
                            65
                        )

                        if start_button.collidepoint(event.pos):

                            self.start_game()

                        elif quit_button.collidepoint(event.pos):

                            self.running = False

                continue

            # -----------------------------
            # KEYBOARD
            # -----------------------------

            if event.type == pygame.KEYDOWN:

                # Player shooting
                if (
                    event.key == pygame.K_SPACE
                    and len(self.enemies) > 0
                    and not self.game_over
                    and not self.wave_transition
                ):

                    self.player.shoot()

                # Restart
                if event.key == pygame.K_r:

                    self.reset_game()

            # -----------------------------
            # ENEMY SHOOTING
            # -----------------------------

            if (
                event.type == self.ENEMY_SHOOT_EVENT
                and len(self.enemies) > 0
                and not self.game_over
                and not self.wave_transition
            ):

                shooters = []

                # Find enemies that are not blocked
                for enemy in self.enemies:

                    enemy_rect = enemy.get_rect()

                    blocked = False

                    for other in self.enemies:

                        if other == enemy:
                            continue

                        other_rect = other.get_rect()

                        if other_rect.y > enemy_rect.y:

                            if (
                                enemy_rect.right > other_rect.left
                                and enemy_rect.left < other_rect.right
                            ):

                                blocked = True

                                break

                    if not blocked:

                        shooters.append(enemy)

                # Select shooters
                if len(shooters) > 0:

                    max_shooters = get_max_shooters(
                        self.wave
                    )

                    selected_shooters = random.sample(
                        shooters,
                        min(
                            max_shooters,
                            len(shooters)
                        )
                    )

                    for shooter in selected_shooters:

                        x, y = shooter.shoot()

                        self.enemy_bullets.append(
                            EnemyBullet(x, y)
                        )

                        # 🔊 ENEMY SHOOT SOUND
                        self.audio.play(
                            "enemy_shoot"
                        )

    # UPDATE

    def update(self):

        # UPDATE BACKGROUND

        self.background.update()

        if self.start_screen:

            return

        # WAVE TRANSITION

        if self.wave_transition:

            if (
                pygame.time.get_ticks()
                - self.wave_start_time
                >= self.wave_transition_time
            ):

                self.wave_transition = False

            return

        # NEXT WAVE

        if (
            len(self.enemies) == 0
            and not self.game_over
        ):

            self.wave += 1

            self.enemies = self.create_wave()

            self.enemy_speed = get_enemy_speed(
                self.wave
            )

            pygame.time.set_timer(
                self.ENEMY_SHOOT_EVENT,
                get_shoot_interval(self.wave)
            )

            self.wave_transition = True

            self.wave_start_time = pygame.time.get_ticks()

            self.enemy_bullets = []

            self.explosions = []

            return

        # GAMEPLAY

        if (
            len(self.enemies) > 0
            and not self.game_over
        ):

            # -----------------------------
            # PLAYER
            # -----------------------------

            self.player.update()

            # -----------------------------
            # ENEMY BULLETS
            # -----------------------------

            for bullet in self.enemy_bullets[:]:

                bullet.update()

                if bullet.off_screen():

                    self.enemy_bullets.remove(
                        bullet
                    )

            # -----------------------------
            # PLAYER COLLISION
            # -----------------------------

            player_rect = pygame.Rect(
                self.player.x,
                self.player.y,
                self.player.width,
                self.player.height
            )

            for bullet in self.enemy_bullets[:]:

                if bullet.get_rect().colliderect(
                    player_rect
                ):

                    self.enemy_bullets.remove(
                        bullet
                    )

                    self.lives -= 1

                    if self.lives <= 0:

                        self.lives = 0

                        # Mark player as destroyed
                        self.player.destroyed = True

                        self.game_over = True

                        # 🔊 PLAYER DESTROY SOUND
                        self.audio.play(
                            "player_destroy"
                        )

                        break

            # -----------------------------
            # ENEMY MOVEMENT
            # -----------------------------

            for enemy in self.enemies:

                enemy.update(
                    self.enemy_speed
                )

            # -----------------------------
            # EDGE DETECTION
            # -----------------------------

            hit_edge = False

            for enemy in self.enemies:

                if (
                    enemy.x <= 0
                    or enemy.x + enemy.width >= WIDTH
                ):

                    hit_edge = True

                    break

            # -----------------------------
            # CHANGE DIRECTION
            # -----------------------------

            if hit_edge:

                self.enemy_speed *= -1

                for enemy in self.enemies:

                    enemy.y += self.enemy_drop

            # -----------------------------
            # PLAYER BULLETS
            # -----------------------------

            for bullet in self.player.bullets[:]:

                for enemy in self.enemies[:]:

                    if bullet.get_rect().colliderect(
                        enemy.get_rect()
                    ):

                        # Remove bullet
                        if bullet in self.player.bullets:

                            self.player.bullets.remove(
                                bullet
                            )

                        # Remove enemy
                        if enemy in self.enemies:

                            self.enemies.remove(
                                enemy
                            )

                            # 💥 CODED ENEMY EXPLOSION
                            self.explosions.append(
                                EnemyExplosion(
                                    enemy.x
                                    + enemy.width // 2,

                                    enemy.y
                                    + enemy.height // 2,

                                    max(
                                        enemy.width,
                                        enemy.height
                                    )
                                )
                            )

                            # 🔊 ENEMY DESTROY SOUND
                            self.audio.play(
                                "enemy_destroy"
                            )

                        # Score
                        self.score += 10

                        break

        # EXPLOSIONS

        for explosion in self.explosions[:]:

            explosion.update()

            if explosion.finished:

                self.explosions.remove(
                    explosion
                )

    # DRAW

    def draw(self):

        # BACKGROUND

        if self.start_screen:

            self.draw_start_screen()
            return

        self.background.draw(
            self.screen
        )

        # ENEMIES

        for enemy in self.enemies:

            enemy.draw(
                self.screen
            )

        # PLAYER

        self.player.draw(
            self.screen
        )

        # ENEMY BULLETS

        for bullet in self.enemy_bullets:

            bullet.draw(
                self.screen
            )

        # EXPLOSIONS

        for explosion in self.explosions:

            explosion.draw(
                self.screen
            )

        # HUD

        self.hud.draw(
            self.screen,
            self.score,
            self.lives,
            self.wave,
            self.game_over,
            self.wave_transition
        )

        # WAVE TRANSITION

        if (
            self.wave_transition
            and not self.game_over
        ):

            elapsed = (
                pygame.time.get_ticks()
                - self.wave_start_time
            )

            progress = (
                elapsed
                / self.wave_transition_time
            )

            if progress > 1:

                progress = 1

            if progress < 0.5:

                fade = progress * 2

            else:

                fade = (1 - progress) * 2

            alpha = int(
                255 * fade
            )

            wave_text = self.big_font.render(
                f"WAVE {self.wave}",
                True,
                WHITE
            )

            ready_text = self.small_font.render(
                "GET READY...",
                True,
                WHITE
            )

            wave_text.set_alpha(
                alpha
            )

            ready_text.set_alpha(
                alpha
            )

            self.screen.blit(
                wave_text,
                (
                    WIDTH // 2
                    - wave_text.get_width() // 2,

                    HEIGHT // 2 - 70
                )
            )

            self.screen.blit(
                ready_text,
                (
                    WIDTH // 2
                    - ready_text.get_width() // 2,

                    HEIGHT // 2 + 10
                )
            )

        # GAME OVER

        if self.game_over:

            # Dark overlay
            overlay = pygame.Surface(
                (WIDTH, HEIGHT),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 100)
            )

            self.screen.blit(
                overlay,
                (0, 0)
            )

            game_over_text = self.big_font.render(
                "GAME OVER",
                True,
                (255, 80, 80)
            )

            restart_text = self.font.render(
                "Press R to Restart",
                True,
                WHITE
            )

            self.screen.blit(
                game_over_text,
                (
                    WIDTH // 2
                    - game_over_text.get_width() // 2,

                    HEIGHT // 2 - 70
                )
            )

            self.screen.blit(
                restart_text,
                (
                    WIDTH // 2
                    - restart_text.get_width() // 2,

                    HEIGHT // 2 + 10
                )
            )

        # DISPLAY

        pygame.display.flip()

    # RUN

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)

        # Stop background music before quitting
        self.audio.stop_music()

        pygame.quit()
