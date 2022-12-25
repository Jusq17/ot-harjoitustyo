
import numpy as np
from logic import gamelogic
from game import game_main
import unittest
import pygame
import sys

class tests(unittest.TestCase):

    def setUp(self):

        self.logic = gamelogic.Logic()
        self.game = game_main.Game()

    def test_start_pos(self):

        count = 0

        self.logic.create_start_pos(self.game.matrix)

        for i in range(0, 3):

            for j in range(0, 3):

                if self.logic.matrix1[i][j] > 0:

                    count += 1

                elif self.logic.matrix1[i][j] > 2:

                    self.assertEqual(True, False)

        self.assertLess(count, 2.1)

    def test_move_left(self):

        result_matrix = np.zeros((4, 4), dtype="int")

        result_matrix[0, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 2] = 2
        self.game.matrix[0, 3] = 2

        self.game.matrix = self.logic.move_left(self.game.matrix)[0]

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            self.assertEqual(True, False)

        self.assertEqual(self.logic.score, 4)

    def test_move_right(self):

        result_matrix = np.zeros((4, 4), dtype="int")

        result_matrix[0, 3] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[0, 1] = 2

        self.game.matrix = self.logic.move_right(self.game.matrix)[0]

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            self.assertEqual(True, False)

        self.assertEqual(self.logic.score, 4)

    def test_move_up(self):

        result_matrix = np.zeros((4, 4), dtype="int")

        result_matrix[0, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[1, 0] = 2

        self.game.matrix = self.logic.move_up(self.game.matrix)[0]

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            self.assertEqual(True, False)

        self.assertEqual(self.logic.score, 4)

    def test_move_down(self):

        result_matrix = np.zeros((4, 4), dtype="int")

        result_matrix[3, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[1, 0] = 2

        self.game.matrix = self.logic.move_down(self.game.matrix)[0]

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            self.assertEqual(True, False)

        self.assertEqual(self.logic.score, 4)

    def test_pygame_key(self):

        dict = {}

        result_matrix = np.zeros((4, 4), dtype="int")
        result_matrix[0, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 2] = 2
        self.game.matrix[0, 3] = 2

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_LEFT
        event = pygame.event.Event(type, dict)

        value = self.game.game_handler(event)

        self.assertEqual(value, "left")

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            print(self.game.matrix)
            print(result_matrix)

            self.assertEqual(self.game.matrix[0,0], result_matrix[0,0])



        dict = {}

        result_matrix = np.zeros((4, 4), dtype="int")
        result_matrix[0, 3] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[0, 1] = 2

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_RIGHT
        event = pygame.event.Event(type, dict)

        value = self.game.game_handler(event)

        self.assertEqual(value, "right")

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            print(self.game.matrix)
            print(result_matrix)

            self.assertEqual(self.game.matrix[0,0], result_matrix[0,0])



        dict = {}

        result_matrix = np.zeros((4, 4), dtype="int")
        result_matrix[3, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[1, 0] = 2

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_DOWN
        event = pygame.event.Event(type, dict)

        value = self.game.game_handler(event)

        self.assertEqual(value, "down")

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            print(self.game.matrix)
            print(result_matrix)

            self.assertEqual(self.game.matrix[0,0], result_matrix[0,0])



        dict = {}

        result_matrix = np.zeros((4, 4), dtype="int")
        result_matrix[0, 0] = 4

        self.game.matrix = np.zeros((4, 4), dtype="int")

        self.game.matrix[0, 0] = 2
        self.game.matrix[1, 0] = 2

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_UP
        event = pygame.event.Event(type, dict)

        value = self.game.game_handler(event)

        self.assertEqual(value, "up")

        if np.array_equal(self.game.matrix, result_matrix):

            self.assertEqual(True, True)

        else:

            print(self.game.matrix)
            print(result_matrix)

            self.assertEqual(self.game.matrix[0,0], result_matrix[0,0])



        dict = {}

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_r
        event = pygame.event.Event(type, dict)

        value = self.game.game_handler(event)

        self.assertEqual(value, "r")

        dict = {}

        type = pygame.KEYDOWN
        dict['unicode'] = None
        dict['key'] = pygame.K_RETURN
        event = pygame.event.Event(type, dict)

        game_state_value = self.game.menu_handler(event)

        self.assertEqual(game_state_value, 1)



if __name__ == "__main__":

    unittest.main()
