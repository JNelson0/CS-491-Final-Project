from snake import snake
from body import body
from segment import segment
from game import game

import pygame

import unittest

class TestGame(unittest.TestCase):
    
    def test_randomSnack(self):
        g = game()
        s = snake((1, 1, 1), (10, 10))
        snackPosition = g.randomSnack(10, s)
        
        ## TEST NEW SNAKE SNACK CREATED
        self.assertTrue(snackPosition)

        ## TEST SNACK NOT IN SAME LOCATION AS SNAKE
        self.assertNotEqual(s.body.head.pos, snackPosition)


class TestSnake(unittest.TestCase):
    
    def test_init(self):
        s = snake((11, 11, 11), (10, 10))
        test = snake((11, 11, 11), (0, 0))

        ## TEST SNAKE COLOR
        self.assertEqual(s.color, test.color)

        ## TEST SNAKE START POSITION
        segmentHead =  segment((10, 10))
        self.assertEqual(s.body.head.pos, segmentHead.pos)

    def test_move(self):
        s = snake((1, 1, 1), (10, 10))

        ## TEST SNAKE MOVE LEFT
        s.move((True, False, False, False))
        self.assertEqual(s.xDir, -1)
        self.assertEqual(s.yDir, 0) 

        ## TEST SNAKE MOVE RIGHT
        s.move((False, True, False, False))
        self.assertEqual(s.xDir, 1)
        self.assertEqual(s.yDir, 0)

        ## TEST SNAKE MOVE UP
        s.move((False, False, True, False))
        self.assertEqual(s.xDir, 0)
        self.assertEqual(s.yDir, -1)

        ## TEST SNAKE MOVE DOWN
        s.move((False, False, False, True))
        self.assertEqual(s.xDir, 0)
        self.assertEqual(s.yDir, 1)

    def test_reset(self):
        s = snake((1, 1, 1), (14, 23))
        s.xDir = -1
        s.yDir = 0
        s.body.parts = [segment(14, 22), segment(14, 21)]
        s.reset((10, 10))

        ## TEST RESET FOR SNAKE X DIRECTION
        self.assertEqual(s.xDir, 0)
        ## TEST RESET FOR SNAKE Y DIRECTION
        self.assertEqual(s.yDir, 1)
        ## TEST RESET FOR SNAKE BODY
        headReset = segment((10, 10))
        self.assertEqual(s.body.parts[0].pos, headReset.pos)


    def test_checkSnake(self):
        pass


class TestBody(unittest.TestCase):
    
    def test_init(self):
        b = body((10, 10))
        self.assertEqual(b.parts[0].pos, (10, 10))

    def test_addBodySegment(self):
        b = body((10, 10))
        b.addBodySegment(segment((b.parts[-1].pos[0] - 1, b.parts[-1].pos[1])))
        self.assertEqual(b.parts[1].pos, (9, 10))

    def test_moveBodyParts(self):
        pass

    def test_checkBodyParts(self):
        b = body((10, 10))
        b.xDir, b.yDir = 1, 0
        ## TEST FOR OUT OF RANGE SNAKE RIGHT
        b.parts.append(segment((20, 10)))
        self.assertTrue(b.checkBodyParts())

        b.xDir, b.yDir = 0, 1
        ## TEST FOR OUT OF RANGE SNAKE DOWN
        b.parts.append(segment((10, 20)))
        self.assertTrue(b.checkBodyParts())

        b.xDir, b.yDir = -1, 0
        ## TEST FOR OUT OF RANGE SNAKE LEFT
        b.parts.append(segment((-1, 10)))
        self.assertTrue(b.checkBodyParts())

        b.xDir, b.yDir = 0, -1        
        ## TEST FOR OUT OF RANGE SNAKE UP
        b.parts.append(segment((10, -1)))
        self.assertTrue(b.checkBodyParts())

        b = body((10, 10))
        self.assertFalse(b.checkBodyParts())
        
    def test_getBodyHead(self):
        b = body((10, 10))
        ## TEST HEAD MATCHES RETURN VALUE
        self.assertEqual(b.getBodyHead(), b.head)

        ## TEST EXPECTED HEAD POS
        self.assertEqual(b.getBodyHead().pos, (10, 10))

class TestSegment(unittest.TestCase):
    
    def test_init(self):
        seg = segment((10, 10))
        test = segment((10, 10))
        self.assertEqual(seg.pos, test.pos)

    def test_move(self):
        seg = segment((10, 10))
        seg.move(1, 0)
        self.assertEqual(seg.pos, (11, 10))

class IntegrationTest(unittest.TestCase):
    
    ##### INTEGRATION TEST FOR ADDING NEW BODY PART TO SNAKE
    ### snake.addToSnake() -> body.addBodySegment()
    def test_addToSnake(self):
        s = snake((1, 1, 1), (10, 10))

        ## TEST ADDING SEGMENT LEFT OF SNAKE
        s.xDir, s.yDir = 1, 0
        s.addToSnake()
        self.assertEqual(s.body.parts[-1].pos, (9, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT RIGHT OF SNAKE
        s.xDir, s.yDir = -1, 0
        s.addToSnake()
        self.assertEqual(s.body.parts[-1].pos, (11, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT DOWN OF SNAKE
        s.xDir, s.yDir = 0, 1
        s.addToSnake()
        self.assertEqual(s.body.parts[-1].pos, (10, 9))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT UP OF SNAKE
        s.xDir, s.yDir = 0, -1
        s.addToSnake()
        self.assertEqual(s.body.parts[-1].pos, (10, 11))

    ##### INTEGRATION TEST FOR RETRIEVING SNAKE HEAD POSITION
    ### game getSnakeHead() -> snake getSnakeHead() -> body getBodyHead()
    def test_getSnakeHead(self):
        g = game()
        s = snake((1, 1, 1), (10, 10))

        ## TEST CORRECT SNAKE HEAD OBJECT RETURNED
        self.assertEqual(g.getSnakeHead(s), s.body.head)

        ## TEST POSITION OF RETRIEVED SNAKE HEAD IS CORRECT
        self.assertEqual(g.getSnakeHead(s).pos, (10, 10))

    ##### INTEGRATION TEST FOR ADDING SEGMENT TO SNAKE BODY
    ### game snakeSnack() -> snake addToSnake() -> body addBodySegment()
    def test_snakeSnack(self):
        g = game()
        s = snake((1, 1, 1), (10, 10))

        ## TEST ADDING SEGMENT TO SNAKE LEFT
        s.xDir, s.yDir = 1, 0
        g.snakeSnack(s)
        self.assertEqual(s.body.parts[-1].pos, (9, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT TO SNAKE RIGHT
        s.xDir, s.yDir = -1, 0
        g.snakeSnack(s)
        self.assertEqual(s.body.parts[-1].pos, (11, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT TO SNAKE DOWN
        s.xDir, s.yDir = 0, 1
        g.snakeSnack(s)
        self.assertEqual(s.body.parts[-1].pos, (10, 9))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT TO SNAKE UP
        s.xDir, s.yDir = 0, -1
        g.snakeSnack(s)
        self.assertEqual(s.body.parts[-1].pos, (10, 11))

    ##### INTEGRATION TEST TO CHECK IF SNAKE IS EITHER OUT OF BOUNDS OR IF THE SNAKE HITS ITS OWN BODY SEGMENT
    ### game checkLoss() -> snake checkSnake -> body checkBodyParts()
    def test_checkLoss(self):
        g = game()
        s = snake((1, 1, 1), (10, 10))
        g.snakeSnack(s)

        ## TEST IF SNAKE IS IN BOUNDS AND NOT HITTING ANOTHER SEGMENT
        self.assertFalse(g.checkLoss(s))

        ## TEST IF SNAKE IS OUT OF BOUNDS (LOSE GAME)
        ## TEST FOR OUT OF RANGE SNAKE DOWN
        s.xDir, s.yDir = 0, 1
        s.body.parts.append(segment((20, 10)))
        self.assertTrue(g.checkLoss(s))

    ##### INTEGRATION TEST FOR INITIALIZING START SNAKE AT START OF GAME
    ### snake __init__() -> body __init__() -> segment __init__()
    ## snake class intializes direction color and body containing list of segments 
    ## body initializes the head of the snake and contains all body segments 
    ## segment is initialized as the head of the snake
    def test_Initialize(self):
        ### Snake gets initialized which creates body and segment
        s = snake((1, 1, 1), (15, 15))

        ### TEST BODY CREATED
        self.assertEqual(s.body.parts[0].pos, (15, 15))

        ### TEST SEGMENT WAS CREATED AND ASSIGNED AS SNAKE HEAD
        self.assertEqual(s.body.head.pos, (15, 15))


if __name__ == '__main__':
    unittest.main()
