import pygame
import pprint
import socket
import time
import datetime
import sys

from pygame.locals import*

import classes.network as network

import classes.EventsFile as EventsFile
import classes.players as players
import classes.platform as platform
import stages as stages

import sessions.mainmenu as MAINMENU_SESSION


hostname = socket.gethostname()

def container(win, DEBUG, username="Player", ipv4=socket.gethostbyname(hostname)):

    clock = pygame.time.Clock()

    """TEMP VARIABLES"""
    id = None
    isRun = True

    myfont = pygame.font.SysFont('Comic Sans MS', 20)


    def debug_overlay(Player, fps):
        fps_text = str(fps)
        pos_text = "Pos(" + str(Player.rect.x) + ":" + str(Player.rect.y)+")"
        momentum_text = "Momentum: "+str(Player.momentum)

        fps = myfont.render(fps_text, False, (255, 0, 0))
        pos = myfont.render(pos_text, False, (255, 0, 0))
        momentum = myfont.render(momentum_text, False, (255, 0, 0))

        win.blit(fps, (10, 5))
        win.blit(pos, (10, 25))
        win.blit(momentum, (10, 45))

    def redrawWin(id):
        win.fill((0, 0, 0))  # Clears screen every frame and Draw Players
        # Players[0].update(win,Stages[0])
        # Players[1].update(win,Stages[0])
        for i in range(len(DATA["players"])):
            # Players[i].update(win,Stages[0])            
            pname = myfont.render(DATA["players"][i].username, True, (255,255,255))
            win.blit(pname, (DATA["players"][i].rect.midtop[0]-(myfont.size(DATA["players"][i].username)[0]//2), DATA["players"][i].rect.midtop[1]-DATA["players"][i].size))
            pygame.draw.rect(win, (0,255,0), DATA["players"][i].rect)
            """ for j in range(len(Players[i].bullets)):
                pygame.draw.rect(win, (255,0,0), Players[i].bullets[j].rect) """
        

        for i in range(len(Stages[0])):
            pygame.draw.rect(win, Stages[0][i].color, Stages[0][i].rect)

        if DEBUG:
            fps = int(round(clock.get_fps(), 0))
            debug_overlay(DATA["players"][id], fps)

        pygame.display.update()

    state = {}

    def eventCheck(event):
        """Current Event list"""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
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
            
            if event.key == pygame.K_SPACE:
                state["m_click"] = True # Shoot bullet
            
        return state

    def main():
        run = True
        print(ipv4)
        n = network.Network(ipv4, 1024*10)
        if n.connect():

            global DATA, Stages
            id = n.recv()
            Stages = n.recv()

            NewUpdate = {}

            while run:
                DATA = n.recv()
                # print(f"{gettime()} : data recieved -> ")
                """Listening to the events """
                for event in pygame.event.get():  # Get all events
                    if event.type == pygame.QUIT:  # QUIT event
                        run = EventsFile.GameQuit()  # returns False

                    # check all events, KEYUP | KEYDOWN
                    NewUpdate = eventCheck(event)

                # Updates game display, essential to refresh every frame
                redrawWin(id)
                #print(NewUpdate)
                n.send(NewUpdate)
                # print(f"{gettime()} : data sent-> {NewUpdate}")
                clock.tick(60)
            pygame.quit()
        else:
            print("NON VALID IP")
            MAINMENU_SESSION.container(win)


    main()

