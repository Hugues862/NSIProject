import pygame
import classes.platform as platform
import classes.screenConvert as convert

def initStages(window): # Don't forget to adjust the size to the screen size

    """Creates Premade stages that we can choose in-game"""
    
    Stage0 = [
        platform.hardPlatform(window, convert.xConvert(window, 10), convert.yConvert(window, 75), convert.xConvert(window, 80), convert.yConvert(window, 5)),
        platform.softPlatform(window, convert.xConvert(window, 15), convert.yConvert(window, 45), convert.xConvert(window, 30), convert.yConvert(window, 2.5)),
        platform.softPlatform(window, convert.xConvert(window, 55), convert.yConvert(window, 45), convert.xConvert(window, 30), convert.yConvert(window, 2.5))
    ]

    Stages = [Stage0]
    return Stages