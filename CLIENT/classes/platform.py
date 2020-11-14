import pygame

class softPlatform(pygame.sprite.Sprite): # Transparent Platforms

    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (0,255,0)
        
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)


class hardPlatform(pygame.sprite.Sprite): # Not yet Hard Platforms

    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (0,255,0)
        
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
