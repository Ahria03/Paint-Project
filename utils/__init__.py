"""
Python treats this folder as a Python Package because of
the __init__. This way we can just Import this file directly
and bring in other imports and settings.
"""

# Period designates to import from folder
from .Settings import *
from .Func import *
from .Button import *
import pygame

# Initialize Pygame and its Font library
pygame.init()
pygame.font.init()

