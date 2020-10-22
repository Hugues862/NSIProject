import pygame
import classes.EventsFile as EventsFile
import classes.players as players
import classes.platform as platform
import stages as stages

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((1200,800))
myfont = pygame.font.SysFont('Comic Sans MS', 30)


Player = players.Player(win,500,500, (1.5,1.5)) # Creates a new player
Stages = stages.initStages(win)


#Event Listener
run = True
while run:

    win.fill((0,0,0)) # Clears screen every frame

    """Listening to the events """
    for event in pygame.event.get(): # Get all events
        
        """Current Event list"""
        if event.type == pygame.QUIT: # QUIT event
            run = EventsFile.GameQuit() # returns False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.m_right = True
            if event.key == pygame.K_LEFT:
                Player.m_left = True
            if event.key == pygame.K_UP:
                Player.jump()
            # debug
            if event.key == pygame.K_s:
                Player.rect.x = 400
                Player.rect.y = 400
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.m_right = False
            if event.key == pygame.K_LEFT:
                Player.m_left = False
    

    Player.update(Stages[0])
    for i in range (len(Stages[0])):
        Stages[0][i].draw()
    
    textsurface = myfont.render(str(str(Player.rect.x)+" : "+str(Player.rect.y)), False, (0, 255, 0))
    win.blit(textsurface,(250,250))
    

    
    pygame.display.update() # Updates game display, essential to refresh every frame
    clock.tick(60)





pygame.quit()

# test