from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialize Window
pygame.display.set_caption("Sample Drawing Game")

run = True # Always initially True
clock = pygame.time.Clock() # Initialize clock
grid = init_grid(ROWS, COLS, BG_COLOR) # Initialize grid
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    # List of Buttons
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(310, button_y, 50, 50, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(FPS) # Only move as fast as FPS
    
    # Check every event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user quit
            run = False
        
        if pygame.mouse.get_pressed()[0]: # If user Left Clicks
            pos = pygame.mouse.get_pos() # Get X,Y Position of Spot Clicked
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    
                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        
                        
    draw(WIN, grid, buttons) # Draw screen
            
pygame.quit()