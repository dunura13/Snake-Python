import pygame
import time
import math
import random


SIZE = 30
BACKGROUND = (44,252,3)

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Snake/apple.png")
        self.parent_screen = parent_screen
        self.x = SIZE + 100
        self.y = SIZE + 3

  
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))

    
    def move(self):
        self.x = random.randint(0,960)
        self.y = random.randint(0,760)




class Snake:
    def __init__(self, parent_window,length):

        self.parent_window = parent_window    # The game window

        self.block = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Snake/square.png")

        self.length = length

        self.blockX = [500] * self.length  # will add 40 into the list "length" amnt of times
        self.blockY = [400] * self.length

        self.blockX_change = 0
        self.blockY_change = 0

        self.direction = "up"

    
    def increase_length(self):
        self.length+=1
        self.blockX.append(-50)
        self.blockY.append(-50)    # random spot (number is irrelvant)
    
    def draw(self):
        for i in range(self.length):
            self.parent_window.blit(self.block,(self.blockX[i],self.blockY[i]))

    
    def move_left(self):
        self.direction = "left"
    
    def move_right(self):
        self.direction = "right" 
    
    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"
    
    def move(self):
        for i in range(self.length-1,0,-1):    # -1 means minus the head. 0 means when to stop. -1 means to count down by -1
            self.blockX[i] = self.blockX[i-1] 
            self.blockY[i] = self.blockY[i-1] 
        
        if self.direction == "up":
            self.blockY[0]-=SIZE
        
        if self.direction == "down":
            self.blockY[0]+=SIZE
        
        if self.direction == "left":
            self.blockX[0]-=SIZE
        
        if self.direction == "right":
            self.blockX[0]+=SIZE






class Game:
    def __init__(self):
        pygame.init()

        # WINDOW
        self.DIMENSIONS = (1000,800)
        self.window = pygame.display.set_mode(self.DIMENSIONS)

        pygame.display.set_caption("Snake")
    

        # SNAKE INSTANCE

        self.num = 3

        self.snake = Snake(self.window,self.num)
        self.snake.draw()

        # APPLE INSTANCE

        self.apple = Apple(self.window)


        # SCORE 
        self.score = 0

    def show_game_over(self):
        self.window.fill(BACKGROUND)
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"GAME OVER", True, (255,255,255))
        line2 = font.render(f"SCORE: {self.snake.length-3}",True,(255,255,255))
        line3 = font.render("Press 'return' to play again",True,(255,255,255))
        self.window.blit(line1,(425,400))
        self.window.blit(line2,(440,450))
        self.window.blit(line3,(345,500))

    def play(self):
        self.snake.draw()
        self.snake.move()
        self.apple.draw()
        self.display_score()


        # SNAKE COLLIDING WITH APPLE
        if self.isCollision(self.snake.blockX[0],self.snake.blockY[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # SNAKE COLIDING WITH ITSELF
        for i in range(3,self.snake.length):
            if self.isCollision(self.snake.blockX[0],self.snake.blockY[0],self.snake.blockX[i],self.snake.blockY[i]):
                raise "Game over"  # This basically raises an "error" 
        

        # SNAKE COLLIDING WITH BORDER

        if self.snake.blockX[0] > 1000 or self.snake.blockX[0] < 0:
            raise "Game Over"

        elif self.snake.blockY[0] > 800 or self.snake.blockY[0] < 0:
            raise "Game over"
    
            
    

    def display_score(self):
        font = pygame.font.SysFont("Ariel",30)
        self.score = font.render(f"Score: {self.snake.length-self.num}", True, (255,255,255))
        self.window.blit(self.score,(50,20))



    def isCollision(self,x1,y1,x2,y2):

        distance = math.sqrt(math.pow(x2-x1,2) +   math.pow(y2-y1,2))
        if distance <= 25:
            return True

        

    


    def run(self):

        running = True
        pause = False

        

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False
                    
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()

                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()

                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    
                    if event.key == pygame.K_RETURN:
                        
                        self.snake.length = 3
                        pause = False

                        self.snake.blockX[0] = 500
                        self.snake.blockY[0] = 400
                        
                        

                    


        

            try:
                if not pause:
                    self.window.fill(BACKGROUND)
                    self.play()
                    time.sleep(0.1)
            
            except Exception as e:
                self.show_game_over()
                pause = True

            pygame.display.update()







# START GAME
if __name__ == '__main__':
    game = Game()
    game.run()








