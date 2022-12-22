
import sys
import pygame
import numpy as np
from logic import gamelogic
from UI import UI

class Game():

    """
        Luokka joka hoitaa pygame-eventtien tarkastuksen.
        Mahdollistaa, että pelaaja voi pelata käyttäen nuolinäppäimiä.

        Attributes:

            game_state: kuvaa pelin tilaa, esim. ollaanko menussa vai pelaamassa.
            logic: pelimatriisia käsittelevä luokka.
            ui: Käyttöliittymää ja grafiikkaa käsittelevä luokka.
            clock: pygame kello, jonka avulla asetetaan framerate.
            size: pygame ikkunan koko
            screen: pygame ikkuna, jolle grafiikat piirretään.

    """

    def __init__(self):

        self.game_state = 0

        self.logic = gamelogic.Logic()
        self.ui = UI.UI()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode(self.size)

    def menu_handler(self, event):

        """
            Metodi, joka hoitaa pygame-eventtien tarkastamisen, kun pelaaja on start-menussa.

            Args:
                
            event: pygame-event, joka tarkastetaan

        """

        self.ui.draw_menu_UI(self.screen)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:

                self.game_state = 1

    def game_handler(self, event):

        """
            Metodi, joka hoitaa pygame-eventtien tarkastamisen, kun pelaaja pelaa peliä.

            Args:
                
            event: pygame-event, joka tarkastetaan

        """

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                matrix_before = self.logic.matrix1.copy()

                self.logic.move_left(self.logic.matrix1)

                if np.array_equal(matrix_before, self.logic.matrix1):
                    pass
                else:
                    self.logic.place_n()

            if event.key == pygame.K_RIGHT:

                matrix_before = self.logic.matrix1.copy()

                self.logic.move_right(self.logic.matrix1)

                if np.array_equal(matrix_before, self.logic.matrix1):

                    print("samat")

                    print(matrix_before)
                    print(self.logic.matrix1)
                else:
                    self.logic.place_n()

            if event.key == pygame.K_UP:

                matrix_before = self.logic.matrix1.copy()

                self.logic.move_up(self.logic.matrix1)

                if np.array_equal(matrix_before, self.logic.matrix1):

                    print("samat")

                    print(matrix_before)
                    print(self.logic.matrix1)
                else:
                    self.logic.place_n()

            if event.key == pygame.K_DOWN:

                matrix_before = self.logic.matrix1.copy()

                self.logic.move_down(self.logic.matrix1)

                if np.array_equal(matrix_before, self.logic.matrix1):

                    print("samat")

                    print(matrix_before)
                    print(self.logic.matrix1)
                else:
                    self.logic.place_n()

            if event.key == pygame.K_r:

                self.logic.create_start_pos()
                self.logic.score = 0

            matrix = self.logic.matrix1
            score = self.logic.score

            self.ui.draw_main_UI(self.screen, matrix, score)

    def event_handler(self):

        """
            Metodi, joka hoitaa pygame-eventtien tarkastamisen.

            Args:
                
            none

        """

        event_list = pygame.event.get()

        for event in event_list:

            if self.game_state == 0:
                self.menu_handler(event)

            elif self.game_state == 1:
                self.game_handler(event)

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

    def run(self):

        """
            Funktio, joka päivittää ruudun kellon määräämällä frameratella.

            Args:

            none

        """

        self.event_handler()
        pygame.display.update()
        self.clock.tick(60)
