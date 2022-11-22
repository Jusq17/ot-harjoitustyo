
import unittest
from gamelogic import logic
import numpy as np

class tests(unittest.TestCase):

    def setUp(self):
        
        self.logic = logic()

    def test_move_left(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,0] = 4

        self.logic.matrix = np.zeros((4,4),dtype="int")

        self.logic.matrix[0,0]=2
        self.logic.matrix[0,1]=2

        print(result_matrix)

        print(self.logic.matrix)

        self.logic.move_left(self.logic.matrix)

        self.assertEqual(self.logic.matrix.all(), result_matrix.all())

    def test_move_right(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,3] = 4

        self.logic.matrix = np.zeros((4,4),dtype="int")

        self.logic.matrix[0,0]=2
        self.logic.matrix[0,1]=2

        print(result_matrix)

        print(self.logic.matrix)

        self.logic.move_right(self.logic.matrix)

        self.assertEqual(self.logic.matrix.all(), result_matrix.all())

    def test_move_up(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[0,0] = 4

        self.logic.matrix = np.zeros((4,4),dtype="int")

        self.logic.matrix[0,0]=2
        self.logic.matrix[1,0]=2

        print(result_matrix)

        print(self.logic.matrix)

        self.logic.move_up(self.logic.matrix)

        self.assertEqual(self.logic.matrix.all(), result_matrix.all())

    def test_move_down(self):

        result_matrix = np.zeros((4,4),dtype="int")

        result_matrix[3,0] = 4

        self.logic.matrix = np.zeros((4,4),dtype="int")

        self.logic.matrix[0,0]=2
        self.logic.matrix[1,0]=2

        print(result_matrix)

        print(self.logic.matrix)

        self.logic.move_down(self.logic.matrix)

        self.assertEqual(self.logic.matrix.all(), result_matrix.all())

if __name__ == "__main__":

    unittest.main()