
from logic import gamelogic

from UI import UI
import pygame as pygame
import numpy as np

#game = logic()

#for i in range(10):

    #game.move_left()

    #print(game)

class Game():

    def __init__(self):

        self.gameState = 1

        self.logic = gamelogic.Logic()
        self.UI = UI.UI()

        pygame.init()
        self.clock = pygame.time.Clock()

        self.size = self.width, self.height = 800, 800

        self.black = (0, 0, 0)

        self.screen = pygame.display.set_mode(self.size)

        self.pointsFont = pygame.font.Font('freesansbold.ttf', 80)

    def run(self):

        event_list = pygame.event.get()

        for event in event_list:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    matrix_before = game.logic.matrix1.copy()

                    game.logic.move_left(game.logic.matrix1)

                    if np.array_equal(matrix_before, game.logic.matrix1):

                        print("samat")
                        
                        print(matrix_before)
                        print(game.logic.matrix1)
                    else:
                        game.logic.place_n()

                if event.key == pygame.K_RIGHT:

                    matrix_before = game.logic.matrix1.copy()

                    game.logic.move_right(game.logic.matrix1)

                    if np.array_equal(matrix_before, game.logic.matrix1):

                        print("samat")
                        
                        print(matrix_before)
                        print(game.logic.matrix1)
                    else:
                        game.logic.place_n()

                if event.key == pygame.K_UP:

                    matrix_before = game.logic.matrix1.copy()

                    game.logic.move_up(game.logic.matrix1)

                    if np.array_equal(matrix_before, game.logic.matrix1):

                        print("samat")
                        
                        print(matrix_before)
                        print(game.logic.matrix1)
                    else:
                        game.logic.place_n()
                if event.key == pygame.K_DOWN:

                    matrix_before = game.logic.matrix1.copy()

                    game.logic.move_down(game.logic.matrix1)

                    if np.array_equal(matrix_before, game.logic.matrix1):

                        print("samat")
                        
                        print(matrix_before)
                        print(game.logic.matrix1)
                    else:
                        game.logic.place_n()

            if event.type == pygame.QUIT:

                    pygame.quit()

                    quit()

            matrix = self.logic.matrix1
            score = self.logic.score

            self.UI.drawUI(self.screen, matrix, score)

            #if game.gameState == 1:

                #l = input("Tee siirtosi: ")

                #if l == "a":

                    #game.logic.move_left(game.matrix)

            pygame.display.update()

            self.clock.tick(60)

game = Game()

game.logic.create_start_pos()

#game.run()
        

while True:

    game.run()

    