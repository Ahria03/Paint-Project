"""
The main settings of the program, there is where
you can edit the window size, color values,
interface font, and frames per second.
"""

# Initialize Pygame and its Font library
import pygame
pygame.init()
pygame.font.init()

# https://www.w3schools.com/colors/colors_picker.asp
# Main Color values in RGB Format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (85, 0, 255)
ORANGE = (255, 102, 0)
YELLOW = (255, 255, 0)

# Base FPS and size of Program
FPS = 120
display_info = pygame.display.Info()
HEIGHT = (display_info.current_h // 100) * 100 - 100
WIDTH = HEIGHT - 100
ROWS = COLS = 50

# Toolbar size and pixel size
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // ROWS

# Base background color and grid lines
BG_COLOR = WHITE
DRAW_GRID_LINES = False


# Return Font at requested Size
def get_font_size(size):
    return pygame.font.SysFont("helvetica", size)


# GREY SHADES
GREYL2 = (0, 0, 0)  # Just Black
GREYL1 = (77, 77, 77)
GREYR1 = (179, 179, 179)
GREYR2 = (204, 204, 204)

# RED SHADES
REDL2 = (102, 0, 0)
REDL1 = (179, 0, 0)
REDR1 = (255, 77, 77)
REDR2 = (255, 153, 153)

# GREEN SHADES
GREENL2 = (0, 77, 0)
GREENL1 = (0, 153, 0)
GREENR1 = (77, 255, 77)
GREENR2 = (204, 255, 204)

# BLUE SHADES
BLUEL2 = (0, 0, 102)
BLUEL1 = (0, 0, 179)
BLUER1 = (77, 77, 255)
BLUER2 = (153, 153, 255)

# PURPLE SHADES
PURPLEL2 = (34, 0, 102)
PURPLEL1 = (59, 0, 179)
PURPLER1 = (136, 77, 255)
PURPLER2 = (187, 153, 255)

# ORANGE SHADES
ORANGEL2 = (102, 41, 0)
ORANGEL1 = (179, 71, 0)
ORNAGER1 = (255, 148, 77)
ORANGER2 = (255, 194, 153)

# YELLOW SHADES
YELLOWL2 = (77, 77, 0)
YELLOWL1 = (153, 153, 0)
YELLOWR1 = (255, 255, 51)
YELLOWR2 = (255, 255, 128)
