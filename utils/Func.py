# Initialize Pygame and its Font library
from .Settings import *

pygame.init()
pygame.font.init()


def init_grid(rows, cols, color):
    """Initialize the drawing grid

    Args:
        rows (int): Num of Rows
        cols (int): Num of Cols
        color (tuple): RGB

    Returns:
        (list): Grid
    """
    grid = []
    for index in range(rows):
        # Add new column
        grid.append([])
        for _ in range(cols):
            grid[index].append(color)
    return grid


def draw_grid(win, grid):
    """Draw Grid containing Pixels and Lines
    to make the cubes in the Program

    Args:
        win: Window Display of Program
        grid (list): Grid containing Pixels
    """
    # Enumerate returns both Element and Index
    for row_index, row in enumerate(grid):
        for col_index, pixel_color in enumerate(row):
            pygame.draw.rect(win, pixel_color, (
                col_index * PIXEL_SIZE,             # X
                row_index * PIXEL_SIZE,             # Y
                PIXEL_SIZE,                         # Width
                PIXEL_SIZE))                        # Height
    # Check if grid lines are flagged to True
    if DRAW_GRID_LINES:
        for row_index in range(ROWS + 1):
            pygame.draw.line(win, BLACK,
                             (0, row_index * PIXEL_SIZE),       # Start Pos
                             (WIDTH, row_index * PIXEL_SIZE))   # End Pos
        for col_index in range(COLS):
            pygame.draw.line(win, BLACK,
                             (col_index * PIXEL_SIZE, 0),
                             (col_index * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_toolbar_bar(win):
    """Draw the Bar on the Toolbar

    Args:
        win: [Program Window]
    """
    pygame.draw.rect(win, BLACK, (
        0,
        HEIGHT - TOOLBAR_HEIGHT + 1,
        WIDTH,
        3))


def draw(win, grid, buttons, shades):
    """Create / Update the Display

    Args:
        win: Window Display of Program
        grid (list): Grid containing Pixels
        buttons (list): List of Button Objects
        shades (list): List of Shade Button Objects
    """
    win.fill(BG_COLOR)  # Reset Window
    draw_grid(win, grid)  # Update Grid
    draw_toolbar_bar(win)  # Update Toolbar
    # Update Buttons
    for button in buttons:
        button.draw(win)
    # Update Shades
    if shades is not None:
        for button in shades:
            button.draw(win)
    pygame.display.update()


def get_row_col_from_pos(pos):
    """Decompose the Position to find Pixel Location

    Args:
        pos (tuple): X,Y

    Returns:
        (tuple): Rol,Col
    """
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    return row, col


def brush(size, pos, grid, drawing_color):
    """[Change the size of the brush]

    Args:
        size ([Int]): [Size of Brush]
        pos ([Tuple]): [Pixel clicked]]
        grid ([List]): [Drawing Grid]
        drawing_color ([Str]): [Color to fill Pixel]
    """
    row, col = get_row_col_from_pos(pos)

    for x in range(size):
        for y in range(size):
            try:
                grid[row + y][col + x] = drawing_color
            except IndexError:
                pass
            try:
                grid[row + y][col - x] = drawing_color
            except IndexError:
                pass
            try:
                grid[row - y][col + x] = drawing_color
            except IndexError:
                pass
            try:
                grid[row - y][col - x] = drawing_color
            except IndexError:
                pass
