import pygame

class bullet():

    def __init__(self, player, xs, ys, xf, yf):

        pygame.sprite.Sprite.__init__(self)
        (self.spdx, self.spdy) = ((xf - xs)/(yf - ys), (yf - ys)/(xf - xs))
        self.color = player.color
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 7, 7)
        self.momentum = [10 * self.spdx, 10 * self.spdy]

    def update(self, Platforms):

        self.globalmove()
        
        self.movex()
