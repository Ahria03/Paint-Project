from .settings import *

# Initialize Pygame and its Font library
pygame.init()
pygame.font.init()

def init_grid(rows, cols, color):
    """[Create Grid to draw into]

    Args:
        rows ([Int]): [Num of Rows]
        cols ([Int]): [Num of Cols]
        color ([Tuple]): [Color Code]

    Returns:
        [List]: [Return the Grid]
    """
    grid = []
    
    for index in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[index].append(color)
            
    return grid
    
def draw_grid(win, grid):
    """[Draw Grid containing Pixels and Draw Grid 
    Lines to make the cubes in the Program]

    Args:
        win ([Tuple]): [Window Display of Program]
        grid ([List]): [Grid containing Pixels]
    """
    for i, row in enumerate(grid): # Enumerate returns both Element and Index
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, 
                                          PIXEL_SIZE, PIXEL_SIZE))
            
    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), 
                             (WIDTH, i * PIXEL_SIZE))
        
        for j in range(COLS):
            pygame.draw.line(win, BLACK, (j * PIXEL_SIZE, 0), 
                             (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT), 1)
            
def draw(win, grid, buttons):
    """[Draw the display and fill it in with 
    Background Color and Buttons]

    Args:
        win ([Tuple]): [Window Display of Program]
        grid ([List]): [Grid containing Pixels]
        buttons ([List]): [List of Button Objects]
    """
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    
    for button in buttons:
        button.draw(win)
    
    pygame.display.update()
    
def get_row_col_from_pos(pos):
    """[Decompose the Position to find Pixel Location]

    Args:
        pos ([Tuple]): [X,Y Coord]

    Returns:
        [Tuple]: [Pixel Location as Row and Col]
    """
    x,y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    
    if row >= ROWS:
        raise IndexError
    
    return row,col

