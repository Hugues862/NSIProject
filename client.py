import pygame
import socket

from pygame.locals import *

import sessions.mainmenu as MAINMENU_SESSION
import sessions.game as GAME_SESSION


pygame.init()
pygame.font.init()
infoObject = pygame.display.Info()
win = pygame.display.set_mode((infoObject.current_w-100, infoObject.current_h-100))

MAINMENU_SESSION.container(win)


# Runs the Game
""" GAME_SESSION.container(win, DEBUG=True)
 """
