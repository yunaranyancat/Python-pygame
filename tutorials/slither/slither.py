import pygame,time,random

def main():
    pygame.init()

    #Hardcoded variables
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,155,0)
    display_width = 800
    display_height = 600
    AppleThickness = 30
    block_size = 20
    FPS = 10
    img = pygame.image.load('./extras/snake_head.png')
    appleimg = pygame.image.load('./extras/apple_img.png')
    icon = pygame.image.load('./extras/icon.png')
    smallfont = pygame.font.SysFont("comicsansms", 25)
    medfont = pygame.font.SysFont("comicsansms", 50)
    largefont = pygame.font.SysFont("comicsansms", 80)

    #pygame display
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Slither')
    pygame.display.set_icon(icon)

    #pygame time
    clock = pygame.time.Clock()

    #functions declaration
    def pause():
        paused = True
        message_to_screen("Paused",black,-100,size="large")
        message_to_screen("Press C to continue or Q to quit.",black,25)
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
            clock.tick(5)

    def score(score):
        text = smallfont.render("score: "+str(score),True,black)
        gameDisplay.blit(text, [0,0])

    def randAppleGen():
        randAppleX = random.randrange(0, display_width-AppleThickness)
        randAppleY = random.randrange(0, display_height-AppleThickness)
        return randAppleX,randAppleY

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
            message_to_screen("Welcome to Slither",green,-100,"large")
            message_to_screen("Eat the apple to become longer but avoid walls or yourself",black,0)
            message_to_screen("Press C to play or Q to quit or P to pause while playing",black,90)
            pygame.display.update()
            clock.tick(15)

    def snake(block_size,snakeList):
        if direction == 0:
            head = pygame.transform.rotate(img, 270)
        elif direction == 1:
            head = pygame.transform.rotate(img, 90)
        elif direction == 2:
            head = img
        else:
            head = pygame.transform.rotate(img, 180)
        gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

        for XnY in snakeList[:-1]:
            pygame.draw.rect(gameDisplay, black,[XnY[0],XnY[1],block_size,block_size])

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
        global direction
        direction = 2
        gameExit = False
        gameOver = False
        lead_x = display_width/2
        lead_y = display_height/2
        lead_x_change = 0
        lead_y_change = 0
        snakeList = []
        snakeLength = 1
        randAppleX,randAppleY = randAppleGen()
        while not gameExit:
            if gameOver == True:
                message_to_screen("Game over",red,y_displace=-15,size="large")
                message_to_screen("Press C to play again or Q to quit",black,50,size="medium")
                pygame.display.update()

            while gameOver == True:
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
                        direction = 1
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        direction = 0
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_UP:
                        direction = 2
                        lead_x_change = 0
                        lead_y_change = -block_size
                    elif event.key == pygame.K_DOWN:
                        direction = 3
                        lead_x_change = 0
                        lead_y_change = block_size
                    elif event.key == pygame.K_p:
                        pause()

            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0: #fixed gameover when snake reach beside the wall
                gameOver=True

            lead_x += lead_x_change
            lead_y += lead_y_change

            gameDisplay.fill(white)

            gameDisplay.blit(appleimg, (randAppleX,randAppleY))

            snakeHead = []
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakeList.append(snakeHead)

            if len(snakeList) > snakeLength:
                del snakeList[0]

            for eachCoord in snakeList[:-1]:
                if eachCoord == snakeHead:
                    gameOver = True

            snake(block_size,snakeList)
            score(snakeLength-1)

            if lead_x > randAppleX - block_size:
                if lead_y >= randAppleY - block_size:
                    if lead_x < randAppleX + AppleThickness:
                        if lead_y < randAppleY + AppleThickness:
                            randAppleX,randAppleY = randAppleGen()
                            snakeLength+=1

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        quit()

    game_intro()
    gameLoop()

if __name__ == '__main__':
    main()