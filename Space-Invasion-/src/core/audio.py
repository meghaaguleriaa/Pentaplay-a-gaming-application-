import pygame


class Audio:

    def __init__(self):

        pygame.mixer.init()

        # =================================================
        # BACKGROUND MUSIC
        # =================================================

        self.music_path = "assets/music/background_music.mp3"

        pygame.mixer.music.load(
            self.music_path
        )

        pygame.mixer.music.set_volume(
            0.60
        )

        # =================================================
        # SOUND EFFECTS
        # =================================================

        self.sounds = {

            "player_shoot": pygame.mixer.Sound(
                "assets/sounds/player_shoot.wav"
            ),

            "enemy_shoot": pygame.mixer.Sound(
                "assets/sounds/enemy_shoot.wav"
            ),

            "enemy_destroy": pygame.mixer.Sound(
                "assets/sounds/enemy_destroy.wav"
            ),

            "player_destroy": pygame.mixer.Sound(
                "assets/sounds/player_destroy.wav"
            )
        }

        # Sound-effect volume
        for sound in self.sounds.values():

            sound.set_volume(0.6)

    # =====================================================
    # MUSIC
    # =====================================================

    def play_music(self):

        pygame.mixer.music.play(-1)

    def stop_music(self):

        pygame.mixer.music.stop()

    # =====================================================
    # SOUND EFFECTS
    # =====================================================

    def play(self, sound_name):

        if sound_name in self.sounds:

            self.sounds[sound_name].play()