import random
import pygame
import os
pygame.mixer.init()

pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)



#creating window (our first task is done by creating the window)
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))



#title of the game(our second task is done by giving the title)
pygame.display.set_caption("Snakesgame")
pygame.display.update()
clock = pygame.time.Clock()

#our 11th task is done by displaying score on the screen
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

#game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x=0
    velocity_y=0
    fps=30
    score=0
    init_velocity=5
    snk_list = []
    snk_length = 1
    food_x = random.randint(40, screen_width/2)
    food_y = random.randint(40, screen_height/2)
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:   
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome() 
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #(our third task is done by creating the quit option)
                    exit_game=True
                
                '''
                if event.type == pygame.KEYDOWN: #(our sixth task is done by moving the snakehead in all direction)
                    if event.key == pygame.K_RIGHT:
                        snake_x+=10
                    if event.key == pygame.K_LEFT:
                        snake_x-=10
                    if event.key == pygame.K_UP:
                        snake_y-=10        
                    if event.key == pygame.K_DOWN:
                        snake_y+=10
                '''
                if event.type == pygame.KEYDOWN: #(our eight task is done by moving the snakehead properly as sixth task wasnot completelytrue)
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y =   0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y =   0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity   
                        velocity_x =   0     
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x =   0
                #our seventh task is done by giving velocity to snakehead (but snakehead will move diagonally)
            snake_x+=velocity_x  
            snake_y+=velocity_y        

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6: #(our tenth task is done by increasing score and putting food again)
                score +=10
                
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)       
                snk_length +=5     
            
                if score>int(hiscore):
                    hiscore = score



            gameWindow.fill(white)           #(our fourth task is done by creating the background of white color))
            text_screen("Score: " + str(score ) +"  Hiscore: "+str(hiscore), red, 5, 5) #(it is 11th task)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size]) #(our fifth task is done by creating snakehead)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size]) #(our ninth task is done by creating food)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True    
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()        
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()