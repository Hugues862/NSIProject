import pygame

class Platform():

    def __init__(self,win,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (0,255,0)
        self.win = win
        (self.screen_width,self.screen_height) = self.win.get_size() 
        
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)


    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
