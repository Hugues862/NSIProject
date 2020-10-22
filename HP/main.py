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


Users = []
Users.append(players.Player(win,500,500, (1,1))) # Creates a new player
Stages = stages.initStages(win)

CamX = 0
CamY = 0


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
                Users[0].m_right = True
            if event.key == pygame.K_LEFT:
                Users[0].m_left = True
            if event.key == pygame.K_UP:
                Users[0].jump()
            # debug
            if event.key == pygame.K_s:
                Users[0].rect.x = 400
                Users[0].rect.y = 400
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Users[0].m_right = False
            if event.key == pygame.K_LEFT:
                Users[0].m_left = False
    

    Users[0].update(Stages[0])
    Users[0].draw((CamX,CamY))
    for i in range (len(Stages[0])):
        Stages[0][i].draw()
    
    textsurface = myfont.render(str(str(Users[0].rect.x)+" : "+str(Users[0].rect.y)), False, (0, 255, 0))
    win.blit(textsurface,(250,250))
    

    
    pygame.display.update() # Updates game display, essential to refresh every frame
    clock.tick(60)





pygame.quit()

# test