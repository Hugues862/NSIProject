import pygame
import classes.platform as platform

def initStages(window): # Don't forget to adjust the size to the screen size

    """Creates Premade stages that we can choose in-game"""
    
    Stage0 = [
        platform.hardPlatform(window, 100, 600, 600, 50),
        platform.softPlatform(window, 175, 350, 200, 25),
        platform.softPlatform(window, (800 - 175 - 200), 350, 200, 25)
    ]

    Stages = [Stage0]
    return Stages