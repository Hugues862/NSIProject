import pygame, pprint 
from pygame.locals import*

import classes.network as network

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
clientID = 0


win = pygame.display.set_mode((1536,864))
myfont = pygame.font.SysFont('Comic Sans MS', 20)



def debug_overlay(Player,fps):
    fps_text = str(fps) 
    pos_text ="Pos(" + str(Player.rect.x) + ":" + str(Player.rect.y)+")"
    momentum_text ="Momentum: "+str(Player.momentum) 
    
    fps = myfont.render(fps_text, False, (255, 0, 0))
    pos = myfont.render(pos_text, False, (255, 0, 0))
    momentum = myfont.render(momentum_text, False, (255, 0, 0))

    win.blit(fps,(10,5))
    win.blit(pos,(10,25))
    win.blit(momentum,(10,45))

def redrawWin():
    win.fill((0,0,0)) # Clears screen every frame


    Player.update(Stages[0])
    Player2.update(Stages[0])

    for i in range (len(Stages[0])):
        Stages[0][i].draw()

    

    if DEBUG:
        fps = int(round(clock.get_fps(),0))
        debug_overlay(Player,fps)


    pygame.display.update()

def eventCheck(event):
    """Current Event list"""
    

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

        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            Player.run = True

        if event.key == pygame.K_RIGHT:
            Player.m_right = False

        if event.key == pygame.K_LEFT:
            Player.m_left = False

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(str(tup[0]) + "," + str(tup[1]))


def main():
    run = True

    n = network.Network()
    startPos = read_pos(n.getPos())

    global Player, Player2, Stages
    Player = players.Player(win,startPos[0],startPos[1], (1.5,1.5)) # Creates a new player
    Player2 = players.Player(win,500,500, (1.5,1.5))
    Stages = stages.initStages(win)

    while run:  
        
        p2Pos = read_pos(n.send(make_pos((Player.rect.x, Player.rect.y))))
        Player2.rect.x = p2Pos[0]
        Player2.rect.y = p2Pos[1]

        """Listening to the events """
        for event in pygame.event.get(): # Get all events
            if event.type == pygame.QUIT: # QUIT event
                run = EventsFile.GameQuit() # returns False

            eventCheck(event) #check all events, KEYUP | KEYDOWN
        
        redrawWin() # Updates game display, essential to refresh every frame
        clock.tick(60)

    pygame.quit()



main()
