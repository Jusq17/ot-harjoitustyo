
import sys

import os

sys.path.append(os.getcwd() + '/..')

import unittest
from logic import gamelogic
import numpy as np

class tests(unittest.TestCase):

    def setUp(self):
        
        self.logic = gamelogic.Logic()

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

    def test_game_over(self):

        result_matrix = np.zeros((4,4),dtype="int")

        self.logic.matrix1 = [[2,4,2,4],
                              [4,2,4,2],
                              [2,4,2,4],
                              [4,2,4,2]]

        self.logic.move_left(self.logic.matrix1)

        self.assertEqual(self.logic.matrix1.all(), result_matrix.all())
        self.assertEqual(self.logic.score, 0)

if __name__ == "__main__":

    unittest.main()