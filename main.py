from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialize Window
pygame.display.set_caption("Sample Drawing Game")

run = True # Always initially True
clock = pygame.time.Clock() # Initialize clock
grid = init_grid(ROWS, COLS, BG_COLOR) # Initialize grid
drawing_color = BLACK
current_shades = []
brush_size = 1

while run:
    clock.tick(FPS) # Only move as fast as FPS
    
    # Check every event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user quit
            run = False
        
        if pygame.mouse.get_pressed()[0]: # If user Left Clicks
            pos = pygame.mouse.get_pos() # Get X,Y Position of Spot Clicked
            try: 
                brush(brush_size, pos, grid, drawing_color)
            except IndexError:
                
                # We've clicked off the drawing, check if we clicked either Button or Shade Button
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
                    # Else its a main color so it opens shades
                    else:
                        current_shades = button.shade
                elif is_shade:
                    drawing_color = shade.color
                              
    draw(WIN, grid, buttons, current_shades) # Draw screen
            
pygame.quit()