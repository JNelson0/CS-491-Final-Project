from snake import snake
from segment import segment
from game import game
import unittest

class TestGame(unittest.TestCase):
    
    def test_randomSnack(self):
        g = game()
        s = snake((1, 1, 1), (10, 10))
        snackPosition = g.randomSnack(10, s)
        
        ## TEST NEW SNAKE SNACK CREATED
        self.assertTrue(snackPosition)

        ## TEST SNACK NOT IN SAME LOCATION AS SNAKE
        self.assertNotEqual(s.head.pos, snackPosition)

    def test_messageBox(self):
        pass

    def test_play(self):
        pass

class TestSnake(unittest.TestCase):
    
    def test_init(self):
        s = snake((11, 11, 11), (10, 10))
        test = snake((11, 11, 11), (0, 0))

        ## TEST SNAKE COLOR
        self.assertEqual(s.color, test.color)

        ## TEST SNAKE START POSITION
        segmentHead =  segment((10, 10))
        self.assertEqual(s.head.pos, segmentHead.pos)

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
        s.body = [segment(14, 22), segment(14, 21)]
        s.reset((10, 10))

        ## TEST RESET FOR SNAKE X DIRECTION
        self.assertEqual(s.xDir, 0)
        ## TEST RESET FOR SNAKE Y DIRECTION
        self.assertEqual(s.yDir, 1)
        ## TEST RESET FOR SNAKE BODY
        headReset = segment((10, 10))
        self.assertEqual(s.body[0].pos, headReset.pos)

    def test_addCube(self):
        s = snake((1, 1, 1), (10, 10))

        ## TEST ADDING SEGMENT LEFT OF SNAKE
        s.xDir, s.yDir = 1, 0
        s.addCube()
        self.assertEqual(s.body[-1].pos, (9, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT RIGHT OF SNAKE
        s.xDir, s.yDir = -1, 0
        s.addCube()
        self.assertEqual(s.body[-1].pos, (11, 10))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT DOWN OF SNAKE
        s.xDir, s.yDir = 0, 1
        s.addCube()
        self.assertEqual(s.body[-1].pos, (10, 9))
        s.reset((10, 10))

        ## TEST ADDING SEGMENT UP OF SNAKE
        s.xDir, s.yDir = 0, -1
        s.addCube()
        self.assertEqual(s.body[-1].pos, (10, 11))

    def test_draw(self):
        pass

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
    
    def test(self):
        pass

    def test(self):
        pass

    def test(self):
        pass

    def test(self):
        pass

    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()
