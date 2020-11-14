import pygame

def xConvert(percent):
    """Gives value of the percentage given of the screen width"""

    (screen_width,screen_height) = (1536,864)

    return screen_width * (percent / 100)

def yConvert(percent):
    """Gives value of the percentage given of the screen width"""

    (screen_width,screen_height) = (1536,864)

    return screen_height * (percent / 100)