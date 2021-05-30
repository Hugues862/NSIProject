import pygame
import sys
import classes.bullet as classBullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, fps, vel=(1.5,1.5)):

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
        self.username = "Player" 
        self.bullets = []

        #game variables
        self.gravity_multiplier = 2.5
        self.jump_momentum = 50
        self.GlobalMomentumMultiplier = 0.90
        self.GlobalMomentumExtremums = [1,-1]
        self.GlobalMaxRunSpd = 7.5
        self.GlobalMaxWalkSpd = 1.5

        self.isJump = False 
        self.on_platform = False

        # Status

        self.status = {
            "health" : 100,
            "attackDamage" : 10,
            "stun" : False,
            "stunTime" : 2.5 * fps,
            "sleep" : False,
            "sleepSpam" : 0,
            "giant" : False,
            "giantTime" : 10 * fps,
            "mini" : False,
            "miniTime" : 10 * fps,
            "bolt" : False,
            "boltTime" : 10 * fps,
            "boltSpd" : (2.25, 2.25),
            "poison" : False,
            "poisonTime" : 10 * fps,
            "strong" : False,
            "strongTime" : 10 * fps,
            "slow" : False,
            "slowTime" : 10 * fps,
            "slowSpd" : (0.75, 0.75)
        }

        self.m_click = False
        


    def update(self, Platforms, fps, players):
    
        self.globalmove()
    
        self.movex()

        if self.m_click:
            self.attack(pygame.mouse.get_pos)

        self.checkStatus(fps)
        
        if self.boundaries("y"):
            self.gravity(Platforms)
        else:
            self.momentum[1] = 0
            if self.rect.y < 0:
                self.rect.y = 0

        self.CollisionCheck(Platforms)
        self.corrections()

        print(self.bullets)

        for b in self.bullets:
            b.update(Platforms, players)
        
        # print(self.run)
    
    def setAttribute(self,att,val):
        if att == 'm_right':
            self.m_right = val
        if att == 'm_left':
            self.m_left = val
        if att == 'run':
            self.run = val
        if att == 'm_click':
            self.m_click = val

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
                    if self.momentum[0] <= self.GlobalMaxRunSpd:
                        self.momentum[0] += self.spx

                else: # Walk Speed
                    if self.momentum[0] <= self.GlobalMaxWalkSpd:
                        self.momentum[0] += self.spx

            if self.m_left: # Left Movement

                if self.run: # Run Speed
                    if self.momentum[0] >= -self.GlobalMaxRunSpd:
                        self.momentum[0] -= self.spx

                else: # Walk Speed
                    if self.momentum[0] >= -self.GlobalMaxWalkSpd:
                        self.momentum[0] -= self.spx

        else:
            self.momentum[0] = 0

    def checkStatus(self, fps):

        if self.status["health"] <= 0:
            # Kill player
            pygame.quit()
            sys.exit()
        
        if self.status["stun"] == True:

            # Change variables to 0 in order to be not movable
            self.momentum[0] = 0

            if self.status["stunTime"] != 0:
                 self.status["stunTime"] -= 1

            else: # Return the player to a normal state
                self.status["stun"] = False
                self.status["stunTime"] = 2.5 * fps

        if self.status["sleep"] == True:

            # Change variables to 0 in order to be not movable
            self.momentum[0] = 0

            if self.status["sleepSpam"] >= 25: # Return the player to a normal state after spam
                self.status["sleep"] = False
                self.status["sleepSpam"] = 0
        
        if self.status["bolt"] == True:

            # Change variables to be fast
            (self.spx, self.spy) = self.status["boltSpd"]
            self.GlobalMaxWalkSpd = 4.5
            self.GlobalMaxRunSpd = 22.5

            if self.status["boltTime"] != 0:
                 self.status["boltTime"] -= 1

            else: # Return the player to a normal state
                self.status["bolt"] = False
                self.status["boltTime"] = 10 * fps
                self.GlobalMaxWalkSpd = 1.5
                self.GlobalMaxRunSpd = 7.5

        if self.status["slow"] == True:

            # Change variables to be slow
            (self.spx, self.spy) = self.status["slowSpd"]
            self.GlobalMaxWalkSpd = 0.75
            self.GlobalMaxRunSpd = 3.75

            if self.status["slowTime"] != 0:
                 self.status["slowTime"] -= 1

            else: # Return the player to a normal state
                self.status["slow"] = False
                self.status["slowTime"] = 10 * fps
                self.GlobalMaxWalkSpd = 1.5
                self.GlobalMaxRunSpd = 7.5

        # mini, giant and poison DOES NOTHING FOR NOW

        if self.status["mini"] == True:
            self.status["mini"] = False

        if self.status["giant"] == True:
            self.status["giant"] = False

        if self.status["poison"] == True:
            self.status["poison"] = False

    def attack(self, mpos):

        if len(self.bullets) < 4:
            self.bullets.append(classBullet.bullet(self, self.rect.x, self.rect.y, mpos[0], mpos[1]))
        self.m_click = False
