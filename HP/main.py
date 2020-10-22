import pygame
import classes.EventsFile as EventsFile
import classes.players as players
import classes.platform as platform
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((800,800))
myfont = pygame.font.SysFont('Comic Sans MS', 30)


Users = []
Platforms = []


Users.append(players.Player(win,500,500, (1,1))) # Creates a new player
Platforms.append(platform.hardPlatform(win,100,600,600,50))
print(Platforms[0].rect.size)
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
    

    Users[0].update(Platforms)
    Platforms[0].draw()
    
    textsurface = myfont.render(str(str(Users[0].rect.x)+" : "+str(Users[0].rect.y)), False, (0, 255, 0))
    win.blit(textsurface,(250,250))
    
    
    pygame.display.update() # Updates game display, essential to refresh every frame
    clock.tick(60)





pygame.quit()

