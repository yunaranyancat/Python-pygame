import pygame

pygame.init()
white = (255,255,255) 
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

#leader of group of blocks /head of snake
lead_x = 300
lead_y = 300
lead_x_change = 0

while not gameExit: #event = change in status, so holding a key will not change an event
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change #iteration of the change while key is down..
    #will produce fast change based on fps.. (while loop move soo fast).. test run module
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black,[lead_x,lead_y,10,10])
    pygame.display.update()
        
pygame.quit()

quit()
