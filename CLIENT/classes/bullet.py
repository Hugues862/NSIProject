import pygame

class bullet(pygame.sprite.Sprite):

    def __init__(self, player, xs, ys, xf, yf):

        pygame.sprite.Sprite.__init__(self)
        (self.spdx, self.spdy) = ((xf - xs)/(yf - ys), (yf - ys)/(xf - xs))
        self.color = player.color
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 10, 10)
        (self.xf, self.yf) = (xf, yf)
        self.momentum = [5 * self.spdx, 5 * self.spdy]
        self.damage = player.status["attackDamage"]

        self.own = player

    def update(self, Platforms, players):

        self.globalmove()

        self.CollisionCheck(Platforms, players)

    def CollisionCheck(self, Platforms, players): # Need Hugues to check what is block hit list

        # Check if we hit a player

        collide = pygame.sprite.spritecollide(self, players, False)
        for block in collide:

            # self.kill() # Destroy Bullet
            block.status["health"] -= self.damage

        # Check and see if we hit a platform

        block_hit_list = pygame.sprite.spritecollide(self, Platforms, False)
        for block in block_hit_list:

            # Kills the bullet if Touches a platform
            pass
            #self.kill()

    def globalmove(self):

        self.rect.x += self.momentum[0] # Horizontal Movement
        self.rect.y += self.momentum[1] # Vertical Movement

        if self.rect == (self.xf, self.yf): # Destroys at destination
            self.kill()

    