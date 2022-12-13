
import sys

import os

sys.path.append(os.getcwd() + '/..')

import unittest
from logic import gamelogic
import numpy as np

class tests(unittest.TestCase):

    def setUp(self):
        
        self.logic = gamelogic.Logic()

    def test_start_pos(self):

        count = 0

        self.logic.create_start_pos()

        for i in range(0,3):

            for j in range(0,3):

                if self.logic.matrix1[i][j] > 0:

                    count += 1

                elif self.logic.matrix1[i][j] > 2:

                    self.assertEqual(True, False)

        self.assertLess(count, 2.1)        

    def test_move_left(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,0] = 4

        self.logic.matrix1 = np.zeros((4,4),dtype="int")

        self.logic.matrix1[0,0]=2
        self.logic.matrix1[0,1]=2

        self.logic.move_left(self.logic.matrix1)

        self.assertEqual(self.logic.matrix1.all(), result_matrix.all())
        self.assertEqual(self.logic.score, 4)

    def test_move_right(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,3] = 4

        self.logic.matrix1 = np.zeros((4,4),dtype="int")

        self.logic.matrix1[0,0]=2
        self.logic.matrix1[0,1]=2

        self.logic.move_right(self.logic.matrix1)

        self.assertEqual(self.logic.matrix1.all(), result_matrix.all())
        self.assertEqual(self.logic.score, 4)

    def test_move_up(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,0] = 4

        self.logic.matrix1 = np.zeros((4,4),dtype="int")

        self.logic.matrix1[0,0]=2
        self.logic.matrix1[1,0]=2

        self.logic.move_up(self.logic.matrix1)

        self.assertEqual(self.logic.matrix1.all(), result_matrix.all())
        self.assertEqual(self.logic.score, 4)

    def test_move_down(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[3,0] = 4

        self.logic.matrix1 = np.zeros((4,4),dtype="int")

        self.logic.matrix1[0,0]=2
        self.logic.matrix1[1,0]=2

        self.logic.move_down(self.logic.matrix1)

        self.assertEqual(self.logic.matrix1.all(), result_matrix.all())
        self.assertEqual(self.logic.score, 4)

if __name__ == "__main__":

    unittest.main()