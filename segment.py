import pygame

class segment(object):
    rows = 20
    w = 500
    def __init__(self,start,xDir=1,yDir=0,color=(255,0,0)):
        self.pos = start
        self.xDir = 1
        self.yDir = 0
        self.color = color

        
    def move(self, xDir, yDir):
        self.xDir = xDir
        self.yDir = yDir
        self.pos = (self.pos[0] + self.xDir, self.pos[1] + self.yDir)

    def draw(self, surface):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        return pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        