import pygame
import EventsFile
pygame.init()

win = pygame.display.set_mode((500,500))


x = 50
y = 50
width = 50
height = 50
vel = 5

#Event Listener
run = True
while run:
    pygame.time.delay(30) # Clock for the game in ms

    keys = pygame.key.get_pressed() #stores in keys all keys that are pressed

    """Key Presses"""
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    


    """Listening to the events """
    for event in pygame.event.get(): #Get all events
        
        """Current Event list"""
        if event.type == pygame.QUIT: #QUIT event
            run = EventsFile.GameQuit() #returns False

    

    



    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0 , 0), (x, y, width, height))
    
    
    pygame.display.update() #update game display, essential to refresh every frame

pygame.quit()




