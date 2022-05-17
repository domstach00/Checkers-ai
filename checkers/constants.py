import pygame

WIDTH = 800
HEIGHT = 800
ROWS, COLS = 8, 8
SQARE_SIZE = WIDTH // COLS

POSSIBLE_MOVES_RADIOUS = 15

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (44, 25))

IS_AI: bool = True
IS_AI_VS_AI: bool = True
AI_WHITE_DEPTH = 4
AI_RED_DEPTH = 4

EVAL_LOCATION_POINTS_COL: dict = {
    "0": 1,
    "1": 2,
    "2": 3,
    "3": 3,
    "4": 3,
    "5": 3,
    "6": 2,
    "7": 1
}

EVAL_LOCATION_POINTS_ROW: dict = {
    "0": 1,
    "1": 2,
    "2": 3,
    "3": 3,
    "4": 3,
    "5": 3,
    "6": 2,
    "7": 1
}
