import pygame
import pygame.mixer
import random
import time

pygame.init()
pygame.mixer.init()

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

#PURRRR
nyansound = pygame.mixer.Sound("./sounds/nyan.wav")
evilsound = pygame.mixer.Sound("./sounds/maniac.wav")

def keysGen():
    key = random.randrange(65,90)
    return chr(key)

def positionGen():
    pos = random.randrange(300)
    return int(pos)

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

def screen_message(msg,color,x_pos,y_pos,size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (displayX/2)+x_pos,(displayY /2)+y_pos
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
        screen_message("Welcome to ..",red,0,-100,"small")
        screen_message("MUSIKEYS",white,0,0,"title")
        screen_message("do not worry, you will know how to play it.",red,0,100,"small")
        screen_message("PRESS SPACE TO CONTINUE.",green,0,200,"small")
        pygame.display.update()
        clock.tick(15)

def gameLoop():

    start = pygame.time.get_ticks()
    score = 0
    gameOver = False
    gameExit = False

    while not gameExit:

        timer = 60
        seconds_passed = (pygame.time.get_ticks() - start)/1000
        print(seconds_passed)
        timer = int(timer - seconds_passed)
        if timer < 0:
            gameOver = True


        newKey = keysGen()
        noUserInput = True


        if gameOver == True:
            evilsound.play()
            mkDisplay.fill(black)
            screen_message("Game Over",red,0,0,size="large")
            screen_message("Final score : "+str(score),white,150,250,"medium")
            pygame.display.update()

        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        mkDisplay.fill(black)
        screen_message(newKey,red,positionGen(),positionGen(),size="small")
        screen_message("Score : "+str(score),white,-250,-300,"medium")
        screen_message("Timer : "+str(timer),white,250,-300,"medium")
        pygame.display.update()

        while noUserInput :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if newKey.lower() == pygame.key.name(event.key):
                        nyansound.play()
                        score +=1
                        noUserInput = False
                    else:
                        noUserInput = False
                        gameOver = True


    pygame.quit()
    pygame.mixer.quit()
    quit()


gameStart()
gameLoop()
