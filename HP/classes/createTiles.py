import pygame

def createTiles(floor1, floor2 = [0], floor3 = [0]):

    """
    floors will be tables with :
        the number of platforms on this floor of the stage
        for each platforms, a table of the spacing from the previous platform and the width of the current one.

        eg. [0] for No platforms, which is also the default argument for Floor 2 and 3
            [2, [200 (space), 300, (width)], [400, 300]] This would make a symetrical platform if the width of the window was 1400 px
            [1, [300, 800]] This would make a centered platform with a window with 1400px
    """

    