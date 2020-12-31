import os
import pygame
import sys
import time
from pygame.locals import *


mainClock = pygame.time.Clock()

# Initialise les modules pygame et autres
pygame.init()
pygame.display.set_caption('GUI')

win = pygame.display.set_mode((1536, 864))

font = [pygame.font.SysFont(None, 60), pygame.font.SysFont(None, 30)]


def draw_text(text, font, color, surface, x, y):
    """
    Afiche le texte
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    """fonction qui run le menu"""
    while True:
        mx, my = pygame.mouse.get_pos()

        """
        TOUT LE STYLE DU MENU AU DESSOU
        """

        # black background, peut etre changé pour une image
        win.fill((0, 0, 0))

        draw_text('GUI', font[0], (255, 255, 255), win, 20, 20)  # Titre

        # definie l'affichage des bouttons, a remplacer par des images a terme
        buttons = []
        buttons.append((pygame.Rect(50, 100, 200, 50), btn1))
        buttons.append((pygame.Rect(50, 200, 200, 50), btn2))
        buttons.append((pygame.Rect(50, 300, 200, 50), btn3))
        buttons.append((pygame.Rect(50, 400, 200, 50), btn4))

        # verifie si les bouttons sont cliqué
        for button in buttons:
            if button[0].collidepoint((mx, my)):
                if click:
                    button[1]()

        # dessine les bouttons a l'écran
        for button in buttons:
            pygame.draw.rect(win, (255, 0, 0), button[0])

        # text buttons
        draw_text('Serv + Client',
                  font[1], (255, 255, 255), win, 70, 110)
        draw_text('Serv + 2x Client',
                  font[1], (255, 255, 255), win, 60, 210)
        draw_text('Serv Only',
                  font[1], (255, 255, 255), win, 70, 310)
        draw_text('Client Only',
                  font[1], (255, 255, 255), win, 70, 410)

        # Systeme de detection de click
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # si ECHAPE retour
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:  # Si CLICK click True
                if event.button == 1:
                    click = True

        # pygame display update
        pygame.display.update()
        mainClock.tick(60)


clientpath = "C:/Users/hugue/Documents/Code/NSI/NSIProject/CLIENT/client.py"
serverpath = "C:/Users/hugue/Documents/Code/NSI/NSIProject/CLIENT/server.py"


def btn1():
    os.system(f'start cmd /k "python {serverpath}"')
    time.sleep(2)
    os.system(f'start cmd /k "python {clientpath}"')


def btn2():
    os.system(f'start cmd /k "python {serverpath}"')
    time.sleep(2)
    os.system(f'start cmd /k "python {clientpath}"')
    os.system(f'start cmd /k "python {clientpath}"')


def btn3():
    os.system(f'start cmd /k "python {serverpath}"')


def btn4():
    os.system(f'start cmd /k "python {clientpath}"')


main_menu()
