import pygame
import time
#GAME OVER functionality

pygame.init()
white = (255,255,255) 
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')


clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25) #(,size) , 

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0
    
    while not gameExit:
        # event
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()
            
            for event in pygame.event.get():
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
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver=True
            
        #logic
        lead_x += lead_x_change
        lead_y += lead_y_change

        #graphic rendering
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black,[lead_x,lead_y,10,10])

        #update
        pygame.display.update()

        clock.tick(FPS)
        
    pygame.quit()
    quit()

gameLoop()