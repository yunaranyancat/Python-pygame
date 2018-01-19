import pygame
import time
import random
#Modifying pause game and game over appearance

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

#Sprite
#img = pygame.image.load('./extras/snake_head.png')
#appleimg = pygame.image.load('./extras/apple_img.png')

#icon = pygame.image.load('./extras/icon.png')
#pygame.display.set_icon(icon)


clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 10

direction = 2

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():

    paused = True

    message_to_screen("Paused",
                        black,
                        -100,
                        size="large")
    message_to_screen("Press C to continue or Q to quit.",
                          black,
                          25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)

        clock.tick(5)

def score(score):
    text = smallfont.render("score: "+str(score),True,black)
    gameDisplay.blit(text, [0,0])

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",
                          green,
                          -100,
                          "large")

        message_to_screen("The objective is to shoot and destroy",
                          black,
                          0)

        message_to_screen("Press C to play or Q to quit or P to pause while playing",
                          black,
                          90)


        pygame.display.update()
        clock.tick(15)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2),(display_height /2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def gameLoop():
    direction = 2
    gameExit = False
    gameOver = False

    while not gameExit:
        if gameOver == True:

            message_to_screen("Game over",
                              red,
                              y_displace=-15,
                              size="large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

        while gameOver == True:
            #gameDisplay.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
