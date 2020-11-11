import pygame

class Item(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.size = 10
    self.color = (255,255,255)
    self.rect = pygame.Rect(800,50,self.size, self.size)
    (self.spx, self.spy) = (1.5,1.5)
    self.momentum = [0,0]
    
    #game variables
    self.gravity_multiplier = 1.5
    self.jump_momentum = 30
    self.GlobalMomentumMultiplier = 0.90
    self.GlobalMomentumExtremums = [1,-1]

    self.on_platform = False




  def defWinSize(self,win):
    (self.screen_width,self.screen_height) = win.get_size() 

  def update(self,win,Platforms):
        self.defWinSize(win)
        
        self.globalmove()
    
        #self.movex()
        
        if self.boundaries("y"):
            self.gravity(Platforms)
        else:
            self.momentum[1] = 0
            if self.rect.y < 0:
                self.rect.y = 0

        self.CollisionCheck(Platforms)
        
        self.corrections()
        
        
        
  def draw(self,win):
    pygame.draw.rect(win, self.color, self.rect)

  def levitation(self):#called in gravity()
    self.rect.y += -100


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
      else:
        self.levitation() #IF on platform then, make object levitate
