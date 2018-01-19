import pygame
import random
import time

pygame.init()

#color config
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

#display config
displayX = 800
displayY = 800

mkDisplay = pygame.display.set_mode((displayX,displayY))
pygame.display.set_caption("MKeys")

#font config
titleFontblack = pygame.font.Font('./fonts/black/black.ttf',70)

smallFontgiveme = pygame.font.Font('./fonts/givemeahand/GiveMeAHand.ttf',30)
mediumFontgiveme = pygame.font.Font('./fonts/givemeahand/GiveMeAHand.ttf',60)
largeFontgiveme = pygame.font.Font('./fonts/givemeahand/GiveMeAHand.ttf',90)


#clock config
clock = pygame.time.Clock()

def keysGen():
    key = random.randrange(65,90)
    return chr(key)

def positionGen():
    posX = random.randrange(displayX)
    posY = random.randrange(displayY)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallFontgiveme.render(text, True, color)
    if size == "medium":
        textSurface = mediumFontgiveme.render(text, True, color)
    if size == "large":
        textSurface = largeFontgiveme.render(text, True, color)
    if size == "title":
        textSurface = titleFontblack.render(text, True, color)
    return textSurface, textSurface.get_rect()

def screen_message(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (displayX/2),(displayY /2)+y_displace
    mkDisplay.blit(textSurf,textRect)

def gameStart():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False

        mkDisplay.fill(black)
        screen_message("Welcome to ..",red,-100,"small")
        screen_message("MUSIKEYS",white,0,"title")
        screen_message("do not worry, you will know how to play it.",red,100,"small")
        screen_message("PRESS SPACE TO CONTINUE.",green,200,"small")
        pygame.display.update()
        clock.tick(15)

def gameLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mkDisplay.fill(white)

    pygame.quit()
    quit()

gameStart()
print(keysGen())
