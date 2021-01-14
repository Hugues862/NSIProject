import pygame
import classes.platform as platform
import classes.screenConvert as convert

def initStages(): # Don't forget to adjust the size to the screen size

    """Creates Premade stages that we can choose in-game"""
    
    Stage0 = [
        platform.hardPlatform(convert.xConvert(10), convert.yConvert(75), convert.xConvert(80), convert.yConvert(5)),
        platform.softPlatform(convert.xConvert(15), convert.yConvert(45), convert.xConvert(30), convert.yConvert(2.5)),
        platform.softPlatform(convert.xConvert(55), convert.yConvert(45), convert.xConvert(30), convert.yConvert(2.5))
    ]

    Stages = [Stage0]
    return Stages