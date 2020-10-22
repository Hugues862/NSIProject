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
    
        self.movex()
        
        if self.boundaries("y"):
            self.gravity()
        else:
            self.momentum[1] = 0
            if self.rect.y < 0:
                self.rect.y = 0

        self.CollisionCheck(Platforms)
        
        
        self.draw()
    
    def CollisionCheck(self,Platforms):
        """
        Collision check function
        - y axis collision only
        """
        # Check and see if we hit anything

        block_hit_list = pygame.sprite.spritecollide(self, Platforms, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.

            if self.momentum[1] > 0:
                self.rect.bottom = block.rect.top
            elif self.momentum[1] < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement

            self.momentum[1] = 0

        #if collison occurs, on_platform = True, else = False
        
        if pygame.sprite.spritecollide(self, Platforms, False):
            self.on_platform = True
        else:
            self.on_platform = False

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
   
    def boundaries(self,axis):
        if axis == "x":
            if self.rect.left >= 0 and self.rect.right <= self.screen_width:
                return True
        elif axis == "y":
            if self.rect.top >= 0 and self.rect.bottom <= self.screen_height:
                return True
        else:
            return False 

    def gravity(self):
        if self.on_platform == False:
            self.momentum[1] += 1

    def movex(self):
        if self.boundaries("x"):
            if self.m_right:
                self.momentum[0] += self.spx
            if self.m_left:
                self.momentum[0] -= self.spx
        else:
            self.momentum[0] = 0

        #check player x border
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0


    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)


