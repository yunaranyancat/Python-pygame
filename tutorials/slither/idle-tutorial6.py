import pygame

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    #space to render graphics
    #i.e : https://www.pygame.org/docs/ref/draw.html
    #x coord is going to right side -> +, y coord is going to down side -> +
    pygame.draw.rect(gameDisplay, black,[400,300,10,100]) #surface,color,x-position,y-posiiton,width,height
    #pygame.draw.rect(gameDisplay, red,[400,300,10,10])
    gameDisplay.fill(red, rect=[200,200,50,50])

    # draw < fill = graphic processing speed
    pygame.display.update()

pygame.quit()

quit()
