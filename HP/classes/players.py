import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,win,x,y,vel):
        pygame.sprite.Sprite.__init__(self)
        (self.spx, self.spy) = vel
        self.color = (255,0,0)
        self.rect = pygame.Rect(x, y, 50, 50)
        self.momentum = [0,0]
        self.m_right = False
        self.m_left = False


        self.win = win
        (self.screen_width,self.screen_height) = self.win.get_size()       

        self.isJump = False
        self.on_platform = False 

        
    def update(self,Platforms):
        self.globalmove()
        
        if self.boundaries("x"):
            self.movex()
        else:
            self.momentum[0] = -self.momentum[0]
        
        self.platform_collide(Platforms)

        if self.boundaries("y"):
            if self.on_platform == False:
                self.gravity()
        else:
            self.momentum[1] = 0
            if self.rect.y < 0:
                self.rect.y = 0
        
        
        self.draw()
    
    def globalmove(self):
        self.momentum[0] = round(self.momentum[0],3)
        self.momentum[1] = round(self.momentum[1],3)
        self.rect.x += self.momentum[0]
        self.rect.y += self.momentum[1]
        print(self.momentum)
        
        if not self.momentum[0] == 0:
            if self.momentum[0] < 1 and self.momentum[0] > 0:
                self.momentum[0] = 0
            if self.momentum[0] > -1 and self.momentum[0] < 0:
                self.momentum[0] = 0
            if self.momentum[0] > 0: 
                self.momentum[0]*= 0.95
            else:
                self.momentum[0]*= 0.95

        if not self.momentum[1] == 0: 
            if self.momentum[0] < 1 and self.momentum[0] > 0:
                self.momentum[0] = 0
            if self.momentum[0] > -1 and self.momentum[0] < 0:
                self.momentum[0] = 0
            if self.momentum[1] > 0: 
                self.momentum[1]*= 0.95
            else: 
                self.momentum[1]*= 0.95
    

    def jump(self):
        if self.isJump == False:
            self.isJump = True
            self.momentum[1] -= 20
            self.isJump = False

    def platform_collide(self,platlist):
        PlatformCollision = pygame.sprite.spritecollide(self, platlist, False) 
        if PlatformCollision:
            self.on_platform = True
            if self.momentum[1] >0:
                self.momentum[1] = 0

        else:
            self.on_platform = False        

    def boundaries(self,axis):
        if axis == "x":
            if self.rect.x >= 0 and self.rect.x <= self.screen_width-self.rect.width:
                return True
        elif axis == "y":
            if self.rect.y >= 0 and self.rect.y <= self.screen_height-self.rect.height:
                return True
        else:
            return False 

 

    def gravity(self):
        self.momentum[1] += 1

    def movex(self):
        if self.m_right:
            self.momentum[0] += self.spx
        if self.m_left:
            self.momentum[0] -= self.spx

    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)


