import pygame
WINDOW_NAME = "Game"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH, SCREEN_HEIGHT = 880, 750
FPS = 90
DRAW_FPS = True
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 180
HAND_HITBOX_SIZE = (60, 80)
MORTY_SIZES = (80, 80)
MORTY_SIZE_RANDOMIZE = (1,2)
RICKS_SIZES = (100, 100)
RICK_SIZE_RANDOMIZE = (1.2, 1.5)
DRAW_HITBOX = False
ANIMATION_SPEED = 0.09
GAME_DURATION = 45
MORTY_SPAWN_TIME = 1
MORTY_MOVE_SPEED = {"min": 1, "max": 6}
RICK_PENALITY = 1

COLORS = {"title": (255, 255, 255), "score": (255, 255, 255), "timer": (255, 255, 255),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (0, 0, 0)}}
MUSIC_VOLUME = 0.5
SOUNDS_VOLUME = 0.2

pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 50)
FONTS["big"] = pygame.font.Font(None, 120)
