import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

from segment import segment
from snake import snake

class game:
    def drawGrid(self, w, rows, surface):
        sizeBtwn = w // rows

        x = 0
        y = 0
        for l in range(rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
            pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
            

    def redrawWindow(self, surface):
        global rows, width, s, snack
        surface.fill((0,0,0))
        s.draw(surface)
        snack.draw(surface)
        self.drawGrid(width,rows, surface)
        pygame.display.update()


    def randomSnack(self, rows, item):

        positions = item.body.parts

        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                continue
            else:
                break
            
        return (x,y)


    def messageBox(self, subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

    def snakeSnack(self, snake):
        snake.addToSnake()

    def getSnakeHead(self, snake):
        return snake.getSnakeHead()
    
    def checkLoss(self, snake):
        return snake.checkSnake()

    def play(self):
        global width, rows, s, snack
        width = 500
        rows = 20
        win = pygame.display.set_mode((width, width))
        s = snake((255,0,0), (10,10))
        snack = segment(self.randomSnack(rows, s), color=(0,255,0))

        clock = pygame.time.Clock()
        
        flag = True
        while flag:
            pygame.time.delay(50)
            clock.tick(8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                keys = pygame.key.get_pressed()
            s.move((keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]))
            
            if self.getSnakeHead(s).pos == snack.pos:
                self.snakeSnack(s)
                snack = segment(self.randomSnack(rows, s), color=(0,255,0))

            if self.checkLoss(s):
                print('Score: ', len(s.body.parts))
                self.messageBox('You Lost!', 'Your Score: {}'.format(len(s.body.parts)))
                s.reset((10,10))
                
            self.redrawWindow(win)

