import pygame

class Player():

    def __init__(self,win,x,y,vel):
        (self.spx, self.spy) = vel
        self.color = (255,0,0)
        self.rect = pygame.Rect(x, y, 50, 50)

        self.m_right = False
        self.m_left = False


        self.win = win
        (self.screen_width,self.screen_height) = self.win.get_size()       

        self.isJump = True
        self.isFall = True 

        
    def update(self,platforms):

        self.movex()
        self.draw()


    def movex(self):
        if self.m_right:
            self.rect.x += self.spx
        if self.m_left:
            self.rect.x -= self.spx

    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)


