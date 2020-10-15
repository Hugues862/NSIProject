import pygame
from player import Player


# Init pygame
pygame.init()

# Create window

running = True
screen = pygame.display.set_mode((800, 600))

player = Player(1, screen)
# Loop to keep the window running and to run functions while it is running

while running :

    screen.blit(player.img, (player.x, player.y)) # Display the player

    for event in pygame.event.get():
        if event.type == pygame.QUIT : # Quits window
            running = False

    if event.type == pygame.KEYDOWN: # Get player input

        if event.key == pygame.K_ESCAPE: # Easier way to quit by pressing Esc
            running = False

        if event.key == pygame.K_LEFT: # Moves Left
            player.move("LEFT")

        if event.key == pygame.K_RIGHT: # Moves Right
            player.move("RIGHT")

        if event.key == pygame.K_UP: # Moves Up
            player.move("UP")

        if event.key == pygame.K_DOWN: # Moves Down
            player.move("DOWN")

    pygame.display.update() # Updates display