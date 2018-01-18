import pygame

pygame.init()
white = (255,255,255) 
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock() #https://www.pygame.org/docs/ref/time.html


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10 #try 2 w 100 fps
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10 #try 2 w 100 fps

    lead_x += lead_x_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black,[lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(15) #set up FPS, popular = 30
    #for changing difficulties in game, it is better to change lead_x_change than changing fps
    #fps will force the processor to move as fast as it could.. 
        
pygame.quit()
quit()
