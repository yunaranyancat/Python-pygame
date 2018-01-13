import pygame

pygame.init()
#color in RGB value (,,,)
white = (255,255,255) #pygame.Color("white")
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) #returns pygame surface object
pygame.display.set_caption('Slither')


gameExit = False

while not gameExit:
    for event in pygame.event.get(): #https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT:
            gameExit = True
            
    gameDisplay.fill(white)
    pygame.display.update()
        
pygame.quit()

quit()
