from .settings import *

class Button:
    # Button Class
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        """[All the Properties of the Button]

        Args:
            x ([Int]): [X Cord]
            y ([Int]): [Y Cord]
            width ([Int]): [Width of Button]
            height ([Int]): [Height of Button]
            color ([Tuple]): [Color Code in RGB]
            text ([Str], optional): [Text if wanted on Button]. Defaults to None.
            text_color ([Tuoke], optional): [Color Code in RGB for Text]. Defaults to BLACK.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        
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