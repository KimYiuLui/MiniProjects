import pygame
import random
from time import sleep
from player import *
from values import *

class RunNJump:
    def __init__(self):
        self.intro = True
        self.player = player(200, 400, 50, 80)
        self.player.vel = 10
        self.score = 0
        self.play = True
        self.gameOver = True
        self.clock = clock
        self.window = window
        self.fontName = fontName
        self.obstacle = obstacle(850, 390, 100,90)

    def PreGame(self):
        while self.intro:
            self.events()

            self.window.fill(gray)
            self.draw_text("Run & Jump", 52 ,red, scrWidth / 2, scrHeight / 10)
            self.draw_text("Jump to avoid the obstacles", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.2))
            self.draw_text("controls:", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.8))
            self.draw_text("'d' to move right", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.4))
            self.draw_text("'s' to move left", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.0))
            self.draw_text("'space' to jump", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.6))
            self.draw_text("'ESC' back to menu", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 4.2))
            self.draw_text("Press SPACE to START", 32 ,red, scrWidth / 2, int(scrHeight / 10 * 9))
        
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE]:
                self.intro =  False
                self.play = True
                self.gameOver = False
                self.score = 0
                self.obstacle.x = 850
                self.Run()

            if keys[pygame.K_ESCAPE]:
                self.gameOver = False
                self.play = False
                self.intro = False
                

            
            pygame.display.flip()

    def Run(self):
         while self.play:
            self.events()
            self.clock.tick(30)
            try:
                self.window.fill((gray))
            except:
                return

            scorefont = font = pygame.font.SysFont("arial", 36)
            scoreText = font.render("Score: " + str(self.score), 1, darkGray)
            self.window.blit(scoreText, (590, 10))           
            newOb= pygame.draw.rect(window, blue ,(self.obstacle.x, self.obstacle.y, self.obstacle.width, self.obstacle.height))
            newP= pygame.draw.rect(window, red ,(self.player.x, self.player.y, self.player.width, self.player.height))
            pygame.draw.rect(window, darkGray,(0, 480, 800, 120))
            self.draw_text("'ESC' back to menu", 36 ,gray, 150, 500) 

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.play = False
                self.intro = False
                self.gameOver = False

            if keys[pygame.K_a] and self.player.x > self.player.vel:
                self.player.x -= self.player.vel

            elif keys[pygame.K_d] and self.player.x < 750 - self.player.width - self.player.vel:
                self.player.x += self.player.vel

            if not(self.player.jumping):
                if keys[pygame.K_SPACE]:
                    self.player.jumping = True
            else:
                if self.player.jumpHeight >= -10:
                    neg = 1
                    if self.player.jumpHeight < 0:
                        neg = -1
                    self.player.y -= (self.player.jumpHeight ** 2) * 0.5 * neg
                    self.player.jumpHeight -= 1
                else:
                    self.player.jumping = False
                    self.player.jumpHeight = 10
            
            self.obstacle.x -= self.obstacle.vel

            if self.obstacle.x <= (0 - self.obstacle.width):
                self.obstacle.vel = random.randint(20, (25 + self.score))
                self.obstacle.x = random.randrange(850, 1000)
                self.score += 1

            if newP.colliderect(newOb):
                self.play = False
                self.gameOver = True
                self.GameOver()

    
            pygame.display.update()  
    
    def GameOver(self):
        while self.gameOver:
            self.events()
            self.window.fill(gray)
            self.draw_text("GAME OVER", 52 ,red, scrWidth / 2, scrHeight / 10)
            self.draw_text("Would you like to play agian?", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.2))
            self.draw_text("Press 'r' to play agian", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.8))
            self.draw_text("Your Score is: " + str(self.score), 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.6))
            self.draw_text("Press 'ESC' to go back to menu", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.2))

            keys = pygame.key.get_pressed() 
            if keys[pygame.K_r]:
                self.intro =  False
                self.play = True
                self.score = 0
                self.obstacle.x = 850
                self.Run()

            if keys[pygame.K_ESCAPE]:
                self.gameOver = False
                self.play = False
                self.intro = False
                
            pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(fontName, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.window.blit(text_surface, text_rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                return


                


            
                
            
         
        