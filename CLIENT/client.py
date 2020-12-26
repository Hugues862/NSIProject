import pygame
import pprint 
import socket
import time
import datetime

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
id = None


win = pygame.display.set_mode((1536,864))
myfont = pygame.font.SysFont('Comic Sans MS', 20)

hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname) #recupers l'adresse IP


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

def redrawWin(id):
    win.fill((0,0,0)) # Clears screen every frame and Draw Players
    #Players[0].update(win,Stages[0])
    #Players[1].update(win,Stages[0])
    for i in range(len(Players)):
        #Players[i].update(win,Stages[0])
        pygame.draw.rect(win, Players[i].color, Players[i].rect)

    for i in range (len(Stages[0])):
        pygame.draw.rect(win, Stages[0][i].color, Stages[0][i].rect)

    

    if DEBUG:
        fps = int(round(clock.get_fps(),0))
        debug_overlay(Players[id],fps)


    pygame.display.update()

state = {}

def eventCheck(event):
    """Current Event list"""

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: # Shift Doesn't work
            state["run"] = False

        # Use of Directional keys

        if event.key == pygame.K_RIGHT:
            state["m_right"] = True

        if event.key == pygame.K_LEFT:
            state["m_left"] = True

        if event.key == pygame.K_UP:
            state["jump"] = True

        # debug
    
        
    if event.type == pygame.KEYUP:

        # Go back to default state when releasing keys

        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            state["run"] = True

        if event.key == pygame.K_RIGHT:
            state["m_right"] = False

        if event.key == pygame.K_LEFT:
            state["m_left"] = False

        if event.key == pygame.K_UP:
            state["jump"] = False
    return state

def gettime():
    dt = datetime.datetime.now()
    ms = str(dt.microsecond)
    return dt.strftime("%H:%M:%S:") + ms[2:]

def main():
    run = True
    n = network.Network(ipv4)
    n.connect()


    global Players, Stages
    id = n.recv()
    Stages = n.recv() 

    while run:  
        data = n.recv()
        #print(f"{gettime()} : data recieved -> ")
        Players = data
        """Listening to the events """
        for event in pygame.event.get(): # Get all events
            if event.type == pygame.QUIT: # QUIT event
                run = EventsFile.GameQuit() # returns False

            NewUpdate = eventCheck(event) #check all events, KEYUP | KEYDOWN
        
        redrawWin(id) # Updates game display, essential to refresh every frame
        n.send(NewUpdate)
        #print(f"{gettime()} : data sent-> {NewUpdate}")
        clock.tick(60)

    pygame.quit()



main()

