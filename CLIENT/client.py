import pygame
import socket

from pygame.locals import *

import sessions.mainmenu as MAINMENU_SESSION
import sessions.game as GAME_SESSION


pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1536, 864))

MAINMENU_SESSION.container(win)


# Runs the Game
""" GAME_SESSION.container(win, DEBUG=True)
 """
