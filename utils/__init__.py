"""
Python treats this folder as a Python Package because of
the __init__. This way we can just Import this file directly
and bring in other imports and settings.
"""

# Period designates to import from folder
from .settings import *
from .drawing import *
from .button import *
import pygame

# Initialize Pygame and its Font library
pygame.init()
pygame.font.init()

