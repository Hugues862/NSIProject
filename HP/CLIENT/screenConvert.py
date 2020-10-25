import pygame

def xConvert(win, percent):
    """Gives value of the percentage given of the screen width"""

    (screen_width,screen_height) = win.get_size()

    return screen_width * (percent / 100)

def yConvert(win, percent):
    """Gives value of the percentage given of the screen width"""

    (screen_width,screen_height) = win.get_size()

    return screen_height * (percent / 100)