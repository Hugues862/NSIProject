import pygame

class baseButton():

    def __init__(self, x, y, width, height, text = "Button", size = 16, color = "#FFFFFF"):
        
        # Button base variables.


        self.text = text
        # self.tColor =
        self.size = size
        self.color = color
        # self.swapColor = 
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(x, y, width, height)

        # Interaction Variables

        self.isHover = False
        

    def update(self):

        posx, posy = pygame.mouse.get_pos()

        buttons = pygame.mouse.get_pressed() 
        # Boolean of three buttons ==> (0, 0, 0)
        # First Boolean = Left Click, Second = Middle, Third = Right

        self.hover(posx, posy)
        self.click(buttons)


    def hover(self, mx, my, margin = 8):

        if mx >= (self.rect.x - margin) and mx <= (self.rect.x + self.rect.width + margin) and my >= (self.rect.y - margin) and my <= (self.rect.y + self.rect.height + margin):

            self.isHover = True
            self.rect.x = self.x - 8
            self.rect.y = self.y - 8
            self.rect.width = self.width + 8
            self.rect.height = self.height + 8

        else:

            self.isHover = False
            self.rect.x = self.x + 8
            self.rect.y = self.y + 8
            self.rect.width = self.width - 8
            self.rect.height = self.height - 8
                
    def click(self, mButton):
    # mButtond need to define with "pygame.mouse.get_pressed()" in client.py

        if self.isHover:
            if mButton[0] == True:
                self.function()
            
    def function(self):
        pass

""" class buttonName(baseButton):

    def __init__(self, x, y, width, height, text = "Button", size = 16, color = "#FFFFFF"):
        super().init()

    def update(self):
        super().update()

    def hover(self, mx, my, margin = 7):
        super().hover()
                
    def click(self, mButton):
        super().click()

    def function(self):
        pass """

class MMButton(baseButton): # Main Menu Button

    def __init__(self, x, y, width, height, text = "Button", size = 16, color = "#FFFFFF"):
        super().init()

    def update(self):
        super().update()

    def hover(self, mx, my, margin = 7):
        super().hover()
                
    def click(self, mButton):
        super().click()

    def function(self):
        pass 