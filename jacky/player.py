import pygame

class Player():
    def __init__(self, number, screen):
        self.img = pygame.image.load('Sett_0.jpg')
        self.id = number
        self.spd = 1
        self.x = 400
        self.y = 300
        
    def move(self, direction):
        if direction == "LEFT":
            self.x -= 0.1 * self.spd

        if direction == "RIGHT":
            self.x += 0.1 * self.spd

        if direction == "UP":
            self.y -= 0.1 * self.spd

        if direction == "DOWN":
            self.y += 0.1 * self.spd