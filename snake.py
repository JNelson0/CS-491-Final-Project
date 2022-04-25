import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

from segment import segment



class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = segment(pos)
        self.body.append(self.head)
        self.xDir = 0
        self.yDir = 1

    def move(self, keys):
     
        if keys[0]:
            self.xDir = -1
            self.yDir = 0
            self.turns[self.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[1]:
            self.xDir = 1
            self.yDir = 0
            self.turns[self.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[2]:
            self.xDir = 0
            self.yDir = -1
            self.turns[self.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[3]:
            self.xDir = 0
            self.yDir = 1
            self.turns[self.head.pos[:]] = [self.xDir, self.yDir]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.xDir == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.xDir == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.yDir == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.yDir == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.xDir,c.yDir)
        

    def reset(self, pos):
        self.head = segment(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.xDir = 0
        self.yDir = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = self.xDir, self.yDir

        if dx == 1 and dy == 0:
            self.body.append(segment((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(segment((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(segment((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(segment((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].xDir = dx
        self.body[-1].yDir = dy
        

    def draw(self, surface):
        for c in self.body:
            c.draw(surface)


