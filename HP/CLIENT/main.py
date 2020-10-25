import pygame, pprint 
from pygame.locals import*

import classes.EventsFile as EventsFile
import classes.players as players
import classes.platform as platform
import stages as stages

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

"""GLOBAL VARIABLES"""
DEBUG = True


"""TEMP VARIABLES"""


win = pygame.display.set_mode((1536,864))
myfont = pygame.font.SysFont('Comic Sans MS', 20)


Player = players.Player(win,500,500, (1.5,1.5)) # Creates a new player
Stages = stages.initStages(win)

def debug_overlay(Player,fps):
    fps_text = str(fps) + "fps" 
    pos_text ="Pos(" + str(Player.rect.x) + ":" + str(Player.rect.y)+")"
    momentum_text ="Momentum: "+str(Player.momentum) 
    
    fps = myfont.render(fps_text, False, (255, 0, 0))
    pos = myfont.render(pos_text, False, (255, 0, 0))
    momentum = myfont.render(momentum_text, False, (255, 0, 0))

    win.blit(fps,(10,5))
    win.blit(pos,(10,25))
    win.blit(momentum,(10,45))


run = True
while run:

    win.fill((0,0,0)) # Clears screen every frame

    """Listening to the events """
    for event in pygame.event.get(): # Get all events
        
        """Current Event list"""
        if event.type == pygame.QUIT: # QUIT event
            run = EventsFile.GameQuit() # returns False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: # Shift Doesn't work
                Player.run = False

            # Use of Directional keys

            if event.key == pygame.K_RIGHT:
                Player.m_right = True

            if event.key == pygame.K_LEFT:
                Player.m_left = True

            if event.key == pygame.K_UP:
                Player.jump()

            # debug
            if event.key == pygame.K_s:
                Player.rect.x = 400
                Player.rect.y = 400
            
        if event.type == pygame.KEYUP:

            # Go back to default state when releasing keys

            if event.key == pygame.K_SPACE:
                Player.run = True

            if event.key == pygame.K_RIGHT:
                Player.m_right = False

            if event.key == pygame.K_LEFT:
                Player.m_left = False
    

    Player.update(Stages[0])
    for i in range (len(Stages[0])):
        Stages[0][i].draw()

    fps = int(round(clock.get_fps(),0))
    if DEBUG:
        debug_overlay(Player,fps)
    
    pygame.display.update() # Updates game display, essential to refresh every frame
    clock.tick(60)

pygame.quit()


