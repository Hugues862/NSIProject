import pygame
import socket

from pygame.locals import *

import game as GAMESESSION


pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1536, 864))

# Runs the Game
GAMESESSION.gamecontainer(win, DEBUG=True)
