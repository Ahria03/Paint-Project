# Import the Utils Package
from utils import *

# Initialize Functionality
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pyxel Art")
run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)

# Default Brush Settings
drawing_color = BLACK
current_shades = []
brush_size = 1

while run:
    clock.tick(FPS)
    for event in pygame.event.get():

        # If the user is quitting the application
        if event.type == pygame.QUIT:
            run = False

        # Check if the user is LEFT-CLICKING represented by the [0]
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                draw(brush_size, pos, grid, drawing_color)
            except IndexError:
                # We've clicked off the drawing, check if a button is clicked
                is_color, button = check_button_clicked(buttons, pos)
                is_shade, shade = check_button_clicked(current_shades, pos)

                if is_color:
                    # If button is Clear, Reset Grid
                    if button.text == "CL":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        current_shades = []
                    # If button is Erase
                    elif button.text == "ER":
                        drawing_color = WHITE
                    # If button changes size
                    if button.change_size():
                        brush_size = button.size
                    # Else it's a main color so it opens shades
                    else:
                        current_shades = button.shade
                elif is_shade:
                    drawing_color = shade.color

    update(WIN, grid, buttons, current_shades)  # Draw screen

pygame.quit()
