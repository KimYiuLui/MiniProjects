import pygame
import random
from values import * 
from gameOne import * 
from gameTwo import *
from gameThree import *

class StartUp:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = window
        pygame.display.set_caption("Simple Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fontName = fontName
        self.gameOne = RunNJump()
        self.gameTwo = Snake()

    def startMenu(self):
            self.events()
            self.window.fill(gray)
            self.draw_text("Simple Pygame Project", 52 ,red, scrWidth / 2, scrHeight / 10)
            self.draw_text("Press 1 for Run & Jump", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.2))
            self.draw_text("Press 2 for Snake", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 1.8))
            self.draw_text("More comming soon", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 2.4)) 
            self.draw_text("might add more to it when i have nothing else to do", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.0))
            self.draw_text("Press 'q' to quit", 26 ,darkGray, scrWidth / 2, int(scrHeight / 5 * 3.6))
            self.draw_text("Made by", 22 ,darkGray, scrWidth / 2, int(scrHeight / 10 * 9))
            self.draw_text("Kim Yiu Lui", 26 ,red, scrWidth / 2, int(scrHeight / 10 * 9.5))

            pygame.display.flip()

            keys = pygame.key.get_pressed() 
            if keys[pygame.K_q]:
                self.running = False
                pygame.quit()
                return
            if keys[pygame.K_1]:
                self.gameOne.intro = True 
                self.gameOne.PreGame()

            if keys[pygame.K_2]:
                self.gameTwo.intro = True
                self.gameTwo.PreGame()
            if keys[pygame.K_3]:
                self.gameThree.intro = True
                self.gameThree.PreGame()
            if keys[pygame.K_4]:
                pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.fontName, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.window.blit(text_surface, text_rect)


game = StartUp()

while game.running: 
    game.startMenu()
    try:
        game.events()
    except:
        pass

