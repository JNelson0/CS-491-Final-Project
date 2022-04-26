from body import body
from segment import segment



class snake(object):
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.body = body(pos)

        self.xDir = 0
        self.yDir = 1

    def move(self, keys):
        if keys[0]:
            self.xDir = -1
            self.yDir = 0
            self.turns[self.body.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[1]:
            self.xDir = 1
            self.yDir = 0
            self.turns[self.body.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[2]:
            self.xDir = 0
            self.yDir = -1
            self.turns[self.body.head.pos[:]] = [self.xDir, self.yDir]

        elif keys[3]:
            self.xDir = 0
            self.yDir = 1
            self.turns[self.body.head.pos[:]] = [self.xDir, self.yDir]

        self.body.moveBodyParts(self.turns)
        

    def reset(self, pos):
        self.body = body(pos)
        self.turns = {}
        self.xDir = 0
        self.yDir = 1


    def addToSnake(self):
        tail = self.body.parts[-1]
        dx, dy = self.xDir, self.yDir

        if dx == 1 and dy == 0:
            self.body.addBodySegment(segment((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.addBodySegment(segment((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.addBodySegment(segment((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.addBodySegment(segment((tail.pos[0],tail.pos[1]+1)))

        self.body.parts[-1].xDir = dx
        self.body.parts[-1].yDir = dy
        

    def draw(self, surface):
        for part in self.body.parts:
            part.draw(surface)

    def checkSnake(self):
        return self.body.checkBodyParts()

    def getSnakeHead(self):
        return self.body.getBodyHead()