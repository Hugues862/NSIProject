import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, vel=(1.5,1.5)):
        pygame.sprite.Sprite.__init__(self)
        (self.spx, self.spy) = vel
        self.color = (255,0,0)
        self.size = 25
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.momentum = [0,0]
        self.m_right = False
        self.m_left = False
        self.run = True # Running default
        (self.screen_width,self.screen_height) = (1536,864) 

        #game variables
        self.gravity_multiplier = 2.5
        self.jump_momentum = 50
        self.GlobalMomentumMultiplier = 0.90
        self.GlobalMomentumExtremums = [1,-1]

        self.isJump = False 
        self.on_platform = False

        # Status

        self.status = {
            "stun" : False,
            "stunTime" : 5 * 1000,
            "sleep" : True,
            "sleepSpam" : 0,
            "giant" : False,
            "giantTime" : 10 * 1000,
            "mini" : False,
            "miniTime" : 10 * 1000,
            "bolt" : False,
            "boltTime" : 10 * 1000,
            "poison" : False,
            "poisonTime" : 10 * 1000,
            "strong" : False,
            "strongTime" : 10 * 1000,
            "slow" : False,
            "slowTime" : 10 * 1000
        }




    def update(self,Platforms):
        
        prevTime = self.get_time()

        self.globalmove()
    
        self.movex()

        self.checkStatus(prevTime)
        
        if self.boundaries("y"):
            self.gravity(Platforms)
        else:
            self.momentum[1] = 0
            if self.rect.y < 0:
                self.rect.y = 0

        self.CollisionCheck(Platforms)
        self.corrections()
        
        """ print(self.run) """
    
    def setAttribute(self,att,val):
        if att == 'm_right':
            self.m_right = val
        if att == 'm_left':
            self.m_left = val
        if att == 'run':
            self.run = val

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
        if block_hit_list:
            self.on_platform = True
        else:
            self.on_platform = False
        
    def corrections(self):
        if self.rect.left < 0:
            self.rect.x = 0
        if self.rect.right > self.screen_width:
            self.rect.x = self.screen_width-self.size
        if self.rect.top < 0:
            self.rect.y = 0
        if self.rect.bottom > self.screen_height:
            self.rect.y = self.screen_height-self.size
        
    def globalmove(self):
        self.rect.x += self.momentum[0]
        self.rect.y += self.momentum[1]
        """ print(self.momentum) """
        
        if self.momentum[0] != 0:
            self.momentum[0] = self.momentum[0]*self.GlobalMomentumMultiplier

        if self.momentum[1] != 0:
            self.momentum[1] = self.momentum[1]*self.GlobalMomentumMultiplier
        
        if self.momentum[0] < self.GlobalMomentumExtremums[0] and self.momentum[0] > self.GlobalMomentumExtremums[1]:
            self.momentum[0] = 0

        if self.momentum[1] < self.GlobalMomentumExtremums[0] and self.momentum[1] > self.GlobalMomentumExtremums[1]:
            self.momentum[1] = 0

        self.momentum[0] = round(self.momentum[0],1)
        self.momentum[1] = round(self.momentum[1],1)

        """ if not self.momentum[0] == 0:
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
                self.momentum[1]*= 0.95 """
    
    def jump(self): # Adds to Vertical Momentum
        if self.isJump == False and self.on_platform or self.isJump == False and self.rect.bottom == self.screen_height:
            self.isJump = True
            self.momentum[1] -= self.jump_momentum
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

    def gravity(self,Platforms):
        if self.on_platform == False:
            self.momentum[1] += self.gravity_multiplier

    def movex(self): # Adds to Horizontal Momentum
        if self.boundaries("x"):

            if self.m_right: # Right Movement

                if self.run: # Run speed
                    if self.momentum[0] <= 7.5:
                        self.momentum[0] += self.spx

                else: # Walk Speed
                    if self.momentum[0] <= 1.5:
                        self.momentum[0] += self.spx

            if self.m_left: # Left Movement

                if self.run: # Run Speed
                    if self.momentum[0] >= -7.5:
                        self.momentum[0] -= self.spx

                else: # Walk Speed
                    if self.momentum[0] >= -1.5:
                        self.momentum[0] -= self.spx

        else:
            self.momentum[0] = 0
    
    
    def get_time(self):
        return pygame.time.get_ticks()
    
    def checkStatus(self, curTime):
        
        if self.status["stun"] == True:

            # Change variables to 0 in order to be not movable
            self.momentum = [0,0]

            if self.status["stunTime"] > 0:
                 self.status["stunTime"] -= self.get_time() - curTime

            else: # Return the player to a normal state
                self.status["stun"] = False
                self.status["stunTime"] = 5 * 1000

        if self.status["sleep"] == True:

            # Change variables to 0 in order to be not movable
            self.momentum = [0,0]

            if self.status["sleepSpam"] >= 25: # Return the player to a normal state after spam
                self.status["sleep"] = False
                self.status["sleepSpam"] = 0
        
        if self.status["bolt"] == True:

            # Change variables to be fast
            self.GlobalMomentumMultiplier = 1.35 # .90 * 1.5

            if self.status["boltTime"] > 0:
                 self.status["boltTime"] -= self.get_time() - curTime

            else: # Return the player to a normal state
                self.status["bolt"] = False
                self.status["boltTime"] = 10 * 1000
                self.GlobalMomentumMultiplier = 0.90
        
        if self.status["slow"] == True:

            # Change variables to be slow
            self.GlobalMomentumMultiplier = 0.45 # .90 / 2

            if self.status["slowTime"] > 0:
                 self.status["slowTime"] -= self.get_time() - curTime

            else: # Return the player to a normal state
                self.status["slow"] = False
                self.status["slowTime"] = 10 * 1000
                self.GlobalMomentumMultiplier = 0.90

        # Does nothing for now

        if self.status["mini"] == True:
            self.status["mini"] = False

        if self.status["giant"] == True:
            self.status["giant"] = False

        if self.status["poison"] == True:
            self.status["poison"] = False