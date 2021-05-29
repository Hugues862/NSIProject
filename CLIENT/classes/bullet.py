import pygame

class bullet():

    def __init__(self, player, xs, ys, xf, yf):

        pygame.sprite.Sprite.__init__(self)
        (self.spdx, self.spdy) = ((xf - xs)/(yf - ys), (yf - ys)/(xf - xs))
        self.color = player.color
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 3, 3)
        (self.xf, self.yf) = (xf, yf)
        self.momentum = [10 * self.spdx, 10 * self.spdy]
        self.damage = player.status["attackDamage"]

        self.own = player

    def update(self, Platforms):

        self.globalmove()

        self.CollisionCheck(Platforms)

    def CollisionCheck(self, Platforms, players): # Need Hugues to check what is block hit list

        # Check if we hit a player

        collide = pygame.sprite.spritecollide(self, players, False)

        # Check and see if we hit anything

        block_hit_list = pygame.sprite.spritecollide(self, Platforms, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.

            if self.momentum[1] > 0:
                self.rect.bottom = block.rect.top
            elif self.momentum[1] < 0:
                self.rect.top = block.rect.bottom

    def globalmove(self):

        self.rect.x += self.momentum[0] # Horizontal Movement
        self.rect.y += self.momentum[1] # Vertical Movement

        if self.rect == (self.xf, self.yf): # Destroys at destination
            self.kill()

    