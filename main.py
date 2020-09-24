import pygame
pygame.init()

'''VARIABLES'''
Width = 1000
Height = 800

'''TEMP VARIABLES'''
running = True
Players = []

win = pygame.display.set_mode((Width, Height))


class Player():
    def __init__(self, x, y, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed
        self.sizex = 50
        self.sizey = 50

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(self.x-self.sizex/2, self.y-self.sizey/2, self.sizex, self.sizey))

def get_keydown():
    for event in key_pressed:
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                return "left"
            if event.key == K_RIGHT:
                return "right"
            if event.key == K_UP:
                return "up"
            if event.key == K_DOWN:
                return "down"
            if event.key == K_SPACE:
                return "space"

def get_keyup():
    for event in key_pressed:
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                return "left"
            if event.key == K_RIGHT:
                return "right"
            if event.key == K_UP:
                return "up"
            if event.key == K_DOWN:
                return "down"
            if event.key == K_SPACE:
                return "space"


Players.append(Player(Width/2, Height/2))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   
    if get_keydown()
    

    '''Draw the Player'''
    Players[0].draw()

    '''Draw the ground'''
    pygame.draw.rect(win, (0, 128, 255), pygame.Rect(100, 600, Width-200, 30))
    
    pygame.display.flip()
pygame.quit()

