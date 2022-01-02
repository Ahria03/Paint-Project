from .settings import *

class Button:
    # Button Class
    def __init__(self, x, y, width, height, color, text=None, 
                 text_color=BLACK, size=None, is_main=None, shade=None):
        """[All the Properties of the Button]

        Args:
            x ([Int]): [X Cord]
            y ([Int]): [Y Cord]
            width ([Int]): [Width of Button]
            height ([Int]): [Height of Button]
            color ([Tuple]): [Color Code in RGB]
            text ([Str], optional): [Text if wanted on Button]. Defaults to None.
            text_color ([Tuple], optional): [Color Code in RGB for Text]. Defaults to BLACK.
            size ([Int]) : [Increase size of Brush]
            main ([Bool]) : [If it is a main Color]
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.size = size
        self.is_main = is_main
        self.shade = shade
        
    def draw(self, win):
        """[Draw the Button]

        Args:
            win ([Tuple]): [Window Display]
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, 
                                           self.width, self.height))
        pygame.draw.rect(win, BLACK, (self.x, self.y, 
                                           self.width, self.height), 2)
        
        if self.text:
            button_font = get_font_size(20)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width()/2,
                     self.y + self.height / 2 - text_surface.get_height()/2))
    
    def clicked(self, pos):
        """[Check if Button has been clicked]

        Args:
            pos ([Tuple]): [X,Y Cords]

        Returns:
            [Bool]: [True or False if Clicked]
        """
        x,y = pos
        
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        
        return True
    
    def change_size(self):
        """[Check if the Button changes Brush Size]

        Returns:
            [Bool]: [True if changes Brush Size]
        """
        return self.size is not None
    
    def is_main_color(self):
        """[Checks if a Button is a Main Color]

        Returns:
            [Bool]: [True if Main Color]
        """
        return self.is_main is not None
    
    def get_shade(self):
        """[Return the Shade List]

        Returns:
            [List]: [List of Shades of the Color]
        """
        return self.shade

def check_button_clicked(list_of_buttons, pos):
    """[More detailed search if a button is clicked]

    Args:
        list_of_buttons ([List]): [List of buttons]
        pos ([tuple]): [X,Y Cords]

    Returns:
        [Tuple]: [With a True if clicked, and Button clicked]
    """
    if list_of_buttons == None:
        return False, None
    for button in list_of_buttons:
        if button.clicked(pos):
            return True, button
    return False, None
            

button_y = HEIGHT - TOOLBAR_HEIGHT/2 + 5

def button_x(button_num):
    """[Better Organize the List of Buttons]

    Args:
        button_num ([Int]): [Button Num]

    Returns:
        [Int]: [X Location]
    """
    return (60 * (button_num-1)) + 10

# Used for moving buttons higher
CONSTANT = 45

grey_buttons = [
    # List of Shades of Grey
    Button(button_x(1), button_y-CONSTANT, 40, 40, GREYL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, GREYL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, GREY),
    Button(button_x(4), button_y-CONSTANT, 40, 40, GREYR1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, GREYR2)
]

red_buttons = [
    # List of Shades of Red
    Button(button_x(1), button_y-CONSTANT, 40, 40, REDL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, REDL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, RED),
    Button(button_x(4), button_y-CONSTANT, 40, 40, REDR1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, REDR2)  
]

blue_buttons = [
    # List of Shades of Blue
    Button(button_x(1), button_y-CONSTANT, 40, 40, BLUEL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, BLUEL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, BLUE),
    Button(button_x(4), button_y-CONSTANT, 40, 40, BLUER1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, BLUER2)
]

green_buttons = [
    # List of Shades of Green
    Button(button_x(1), button_y-CONSTANT, 40, 40, GREENL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, GREENL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, GREEN),
    Button(button_x(4), button_y-CONSTANT, 40, 40, GREENR1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, GREENR2)  
]

orange_buttons = [
    # List of Shades of Orange
    Button(button_x(1), button_y-CONSTANT, 40, 40, ORANGEL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, ORANGEL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, ORANGE),
    Button(button_x(4), button_y-CONSTANT, 40, 40, ORNAGER1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, ORANGER2)  
]

yellow_buttons = [
    # List of Shades of Yellow
    Button(button_x(1), button_y-CONSTANT, 40, 40, YELLOWL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, YELLOWL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, YELLOW),
    Button(button_x(4), button_y-CONSTANT, 40, 40, YELLOWR1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, YELLOWR2)  
]

purple_buttons = [
    # List of Shades of Purple
    Button(button_x(1), button_y-CONSTANT, 40, 40, PURPLEL2),
    Button(button_x(2), button_y-CONSTANT, 40, 40, PURPLEL1),
    Button(button_x(3), button_y-CONSTANT, 40, 40, PURPLE),
    Button(button_x(4), button_y-CONSTANT, 40, 40, PURPLER1),
    Button(button_x(5), button_y-CONSTANT, 40, 40, PURPLER2)
]

buttons = [
    # List of Buttons
    Button(button_x(1), button_y, 40, 40, BLACK, is_main=True, shade=grey_buttons),
    Button(button_x(2), button_y, 40, 40, RED, is_main=True, shade=red_buttons),
    Button(button_x(3), button_y, 40, 40, BLUE, is_main=True, shade=blue_buttons),
    Button(button_x(4), button_y, 40, 40, GREEN, is_main=True, shade=green_buttons),
    Button(button_x(5), button_y, 40, 40, ORANGE, is_main=True, shade=orange_buttons),
    Button(button_x(6), button_y, 40, 40, YELLOW, is_main=True, shade=yellow_buttons),
    Button(button_x(7), button_y, 40, 40, PURPLE, is_main=True, shade=purple_buttons),
    Button(button_x(8), button_y, 40, 40, WHITE, "ER", BLACK),
    Button(button_x(9), button_y, 40, 40, WHITE, "CL", BLACK, 1),
    Button(button_x(10), button_y, 40, 40, WHITE, "S1", BLACK, 1),
    Button(button_x(11), button_y, 40, 40, WHITE, "S2", BLACK, 2),
    Button(button_x(12), button_y, 40, 40, WHITE, "S3", BLACK, 3),
    Button(button_x(13), button_y, 40, 40, WHITE, "S5", BLACK, 5),
    Button(button_x(8), button_y-CONSTANT, 40, 40, RED, "BU", BLACK)
]