import pygame
import sys
import random
from player import *
from values import *

class Snake:
    def __init__(self):
        self.intro = True
        self.play = True
        self.gameOver = True
        self.score = 0
        self.clock = clock
        self.window = window
        self.fontName = fontName
        self.snake = player(10,10,20,20)
        self.head = 0
        self.direction = "RIGHT"

        #grid elements
        self.cellsize = 20
        self.cellWidth = int(scrWidth / self.cellsize)
        self.cellHeight = int(500 / self.cellsize)
     

    def PreGame(self):
        while self.intro:
            self.events()

            self.window.fill(gray)
            self.draw_text("Run & Jump", 52 ,red, scrWidth / 2, scrHeight / 10)
            self.draw_text("Eat the Red Blocks", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.2))
            self.draw_text("controls:", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.6))
            self.draw_text("'d' to move right", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.0))
            self.draw_text("'a' to move left", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.4))
            self.draw_text("'w' to move up", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.8)) 
            self.draw_text("'s'to move down", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.2))
            self.draw_text("'ESC' back to menu", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 4.2))
            self.draw_text("Press SPACE to START", 32 ,red, scrWidth / 2, int(scrHeight / 10 * 9))
        
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE]:
                self.intro =  False
                self.play = True
                self.gameOver = False
                self.score = 0
                self.Run()

            if keys[pygame.K_ESCAPE]:
                self.gameOver = False
                self.play = False
                self.intro = False
                return
                

            
            pygame.display.flip()

    def Run(self):
         snakeList = [[self.snake.x, self.snake.y], [self.snake.x - 1, self.snake.y], [self.snake.x - 2, self.snake.y]]
         food = self.generateXY()
         while self.play:
            self.events()

            self.window.fill((gray))
            scorefont = font = pygame.font.SysFont("arial", 36)
            scoreText = font.render("Score: " + str(self.score), 1, gray)     
            pygame.draw.rect(self.window, darkGray,(0, 500, 800, 120))
            self.draw_text("'ESC' back to menu", 36 ,gray, 150, 530) 
            self.window.blit(scoreText, (530, 530)) 

            self.DrawGrid()
            self.DrawSnake(snakeList)
            self.DrawFood(food)

            keys = pygame.key.get_pressed()
  
            if keys[pygame.K_ESCAPE]:
                self.play = False
                self.intro = False
                self.gameOver = False
                return

            # change direction
            elif keys[pygame.K_d] and self.direction != "LEFT":
                self.direction = "RIGHT"
            elif keys[pygame.K_a] and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif keys[pygame.K_w] and self.direction != "DOWN":       
                self.direction = "UP"
            elif keys[pygame.K_s] and self.direction != "UP":     
                self.direction = "DOWN"


            
            # check if snake has hit the wall 
            if snakeList[self.head][0] == -1 or snakeList[self.head][0] == self.cellWidth or snakeList[self.head][1] == -1 or snakeList[self.head][1] == self.cellHeight :
                self.play = False
                self.gameOver = True    
                self.GameOver()
            #check if snake has hit itself
            for segments in snakeList[1:]:
                if  segments[0] == snakeList[self.head][0] and segments[1] == snakeList[self.head][1]:
                    self.play = False
                    self.intro = False
                    self.gameOver = True    
                    self.GameOver()                       
            #generate food if food has been eaten
            if snakeList[self.head][0] == food[0] and snakeList[self.head][1] == food[1]:
                self.score += 1
                food = self.generateXY()
            else:
                del snakeList[-1]

            if self.direction == "LEFT":
                headpos = [snakeList[self.head][0] - 1, snakeList[self.head][1]]
            elif self.direction == "RIGHT":
                headpos = [snakeList[self.head][0] + 1, snakeList[self.head][1]]
            elif self.direction == "UP":
                headpos = [snakeList[self.head][0], snakeList[self.head][1] - 1]
            elif self.direction == "DOWN":
                headpos = [snakeList[self.head][0], snakeList[self.head][1] + 1]
            snakeList.insert(self.head, headpos)
       
            pygame.display.update()    
            self.clock.tick(15)
        
    def GameOver(self):
        while self.gameOver:
            self.window.fill(gray)            
            self.events()
            self.draw_text("GAME OVER", 52 ,red, scrWidth / 2, scrHeight / 10)
            self.draw_text("Would you like to play agian?", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.2))
            self.draw_text("Press 'r' to play agian", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.8))
            self.draw_text("Your Score is: " + str(self.score), 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.6))
            self.draw_text("Press 'ESC' to go back to menu", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.2))

            keys = pygame.key.get_pressed() 
            if keys[pygame.K_r]:
                self.score = 0
                self.intro =  False
                self.play = True
                self.direction = "RIGHT"
                self.Run()

            if keys[pygame.K_ESCAPE]:
                self.gameOver = False
                self.play = False
                self.intro = False
                return
                
            pygame.display.flip()

    def DrawSnake(self, SnakePos):
        for pos in SnakePos:
            x = pos[0] * self.cellsize
            y = pos[1] * self.cellsize
            wormRect = pygame.Rect(x, y, self.cellsize , self.cellsize)
            pygame.draw.rect(self.window, (0, 0, 0), wormRect)
            separationBorder = pygame.Rect(x + 2, y + 2, self.cellsize - 4, self.cellsize - 4)    
            pygame.draw.rect(self.window, darkGray, separationBorder)            

    def generateXY(self):
        return [random.randint(0, self.cellWidth - 1), random.randint(0, self.cellHeight - 2)]

    def DrawFood(self, posXY):
        foodX = posXY[0] * self.cellsize
        foodY = posXY[1] * self.cellsize
        foodRect = pygame.Rect(foodX, foodY, self.cellsize, self.cellsize)
        pygame.draw.rect(self.window, red, foodRect)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(fontName, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.window.blit(text_surface, text_rect)

    def DrawGrid(self):
        for x in range(0, scrWidth, self.cellsize):
            pygame.draw.line(self.window, (255,255,255), (x,0), (x, 500))
        for y in range(0, 520, self.cellsize):
            pygame.draw.line(self.window, (255,255,255), (0,y), (scrWidth,y))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.intro = False
                self.play = False
                self.gameOver = False
                pygame.quit()
                return

