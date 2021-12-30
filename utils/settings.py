import pygame

# Initialize Pygame and its Font library
pygame.init()
pygame.font.init()

# Different Colors in RGB Format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# Base FPS and size of Program
FPS = 60
WIDTH, HEIGHT = 600, 700
ROWS = COLS = 100

# Toolbar size and pixel size
# Does not need to be touched, change prior info instead.
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // ROWS

# Base background color
BG_COLOR = WHITE
DRAW_GRID_LINES = False

def get_font_size(size):
    """[Create a font of whatever size is given]

    Args:
        size ([Int]): [Size of Font]

    Returns:
        [String]: [The font Comic Sans in size]
    """
    return pygame.font.SysFont("timesnewroman", size)