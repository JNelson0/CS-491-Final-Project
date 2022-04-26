from segment import segment

class body(object):

    def __init__(self, pos):
        self.parts = []
        self.head = segment(pos)
        self.parts.append(self.head)

    def addBodySegment(self, segment):
        self.parts.append(segment)

    def moveBodyParts(self, turns):
        for i, part in enumerate(self.parts):
            p = part.pos[:]
            if p in turns:
                turn = turns[p]
                part.move(turn[0],turn[1])
                if i == len(self.parts)-1:
                    turns.pop(p)
            else:
                part.move(part.xDir,part.yDir)

    def checkBodyParts(self):
        for x in range(len(self.parts)):
            if self.parts[x].pos in list(map(lambda z:z.pos, self.parts[x+1:])):
                return True
            elif self.parts[x].xDir == -1 and self.parts[x].pos[0] < 0: 
                return True
            elif self.parts[x].xDir == 1 and self.parts[x].pos[0] > 19: 
                return True
            elif self.parts[x].yDir == 1 and self.parts[x].pos[1] > 19: 
                return True
            elif self.parts[x].yDir == -1 and self.parts[x].pos[1] < 0: 
                return True
        return False

    def getBodyHead(self):
        return self.head