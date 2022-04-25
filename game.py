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

        positions = item.body

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



    def play(self):
        global width, rows, s, snack
        width = 500
        rows = 20
        win = pygame.display.set_mode((width, width))
        s = snake((255,0,0), (10,10))
        snack = segment(self.randomSnack(rows, s), color=(0,255,0))
        flag = True

        clock = pygame.time.Clock()
        
        while flag:
            pygame.time.delay(50)
            clock.tick(8)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
            s.move((keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]))
            
            if s.body[0].pos == snack.pos:
                s.addCube()
                snack = segment(self.randomSnack(rows, s), color=(0,255,0))

            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                    print('Score: ', len(s.body))
                    self.messageBox('You Lost!', 'Play again...')
                    s.reset((10,10))
                    break

                
            self.redrawWindow(win)

