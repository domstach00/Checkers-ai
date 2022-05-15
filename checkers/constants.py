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
