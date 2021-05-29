import pygame
import pygame_menu
import sys
from pygame.locals import *

import sessions.game as GAME_SESSION






def container(win):
    global username
    global ip
    global RUN
    username = "Player"
    ip = "127.0.0.1"
    RUN = True
    def updateip(value):
        global ip
        ip = value

    def updateusername(value):
        global username
        username = value
    
    mainClock = pygame.time.Clock()
    
    # Initialise les modules pygame et autres
    pygame.init()
    pygame.display.set_caption('game base')
    while RUN:
        menu = pygame_menu.Menu(300, 400, 'Welcome',
                        theme=pygame_menu.themes.THEME_DARK)
        menu.add.text_input('', textinput_id="username", default=username, onchange=updateusername)
        menu.add.text_input('', textinput_id="ip", default=ip, onchange=updateip)
        
        def start():
            global RUN
            print(ip, username)
            RUN = False
            if ip == '':
                GAME_SESSION.container(win, DEBUG=True, username=username)
            else:
                GAME_SESSION.container(win, DEBUG=True, username=username, ipv4=ip)
        
        menu.add.button('START', start)

        menu.mainloop(win)


    ''' def draw_text(text, font, color, surface, x, y):
        """
        Afiche le texte
        """
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu():
        click = False
        """fonction qui run le menu"""
        while True:
            mx, my = pygame.mouse.get_pos()

            """
            TOUT LE STYLE DU MENU AU DESSOU
            """

            # black background, peut etre changé pour une image
            win.fill((0, 0, 0))

            draw_text('main menu', font, (255, 255, 255), win, 20, 20)  # Titre

            # definie l'affichage des bouttons, a remplacer par des images a terme
            button_1 = pygame.Rect(50, 100, 200, 50)
            button_2 = pygame.Rect(50, 200, 200, 50)

            # verifie si les bouttons sont cliqué
            if button_1.collidepoint((mx, my)):
                if click:
                    GAME_SESSION.container(win, DEBUG=True)
            if button_2.collidepoint((mx, my)):
                if click:
                    options()

            # dessine les bouttons a l'écran
            pygame.draw.rect(win, (255, 0, 0), button_1)
            pygame.draw.rect(win, (255, 0, 0), button_2)

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

    def options():
        running = True
        while running:
            win.fill((0, 0, 0))

            draw_text('options', font, (255, 255, 255), win, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    main_menu()'''
