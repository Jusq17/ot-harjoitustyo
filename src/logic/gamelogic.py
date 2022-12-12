#Kaikki itse pelin logikkan liittyvät funktiot ovat tässä tiedostossa
#Esim. 2048 "laudan" "siirto" vasempaan ja oikeaan suuntaan.

import numpy as np
import random

import os
print (os.getcwd())

class Logic:

    """
        Luokka, joka käsittelee kaiken pelimatriisiin liittyvän. Sisältää metodit, jotka muokkaavat ja tarkastavat sitä.

        Attributes:

            boardSize: Pelimatriisin/laudan koko
            matrix1: Pelimatriisi
            score: Pelin nykyinen score
            highscore: Paras score, jonka pelaaja on joskus saanut. Tallenetaan highscore.txt tiedostoon.
    """

    def __init__(self):

        #luodaan pelimatriisi("lauta")
        
        self.boardSize = 4
        self.matrix1 = np.zeros((self.boardSize,self.boardSize),dtype="int")

        f = open("src/logic/highscore.txt", "r")
        content = f.readlines()

        f.close()


        self.score = 0
        self.highscore = int(content[0])

    def __str__(self):

        return str(self.matrix)

    def matrix(self):

        return self.matrix1

    def Score(self):

        return str(self.score)

    def place_n(self):

        empty_spaces = []

        n1 = random.randint(0,3)
        n2 = random.randint(0,3)

        for i in range(0,4):

            for j in range(0,4):

                if self.matrix1[i,j] == 0:

                    empty_spaces.append((i,j))

        new_place = random.choice(empty_spaces)

        empty_spaces = []

        self.matrix1[new_place] = 2

    def create_start_pos(self):

        #kuinka monta numeroa pelin alussa on
        start_numbers_n = 2

        #luodaan indeksit joihin numerot laitetaan ja asetetaan numerot sinne

        for i in range(start_numbers_n):

            n1 = random.randint(0,3)
            n2 = random.randint(0,3)

            self.matrix1[n1,n2] = 2

    def is_game_over(self):

        full = False

        if self.matrix1.all() != 0:

            full = True

        transposed_matrix = np.transpose(self.matrix1)

        if full == True:

            for i in range(0,3):

                for j in range(0,3):

                    if self.matrix1[i][j] == self.matrix1[i][j+1]:

                        return False

                    if transposed_matrix[i][j] == transposed_matrix[i][j+1]:

                        return False


            print("Score nollataan")
            print(self.matrix1)

            return True

        else:
       
            return False

    def move_n_left(self, row):

        for l in range(self.boardSize-1):

            if row[l] == 0 and row[l+1] != 0:

                row[l+1], row[l] = row[l], row[l+1]

        return row

    def move_row_left(self, row):

        for l in range(self.boardSize):

            row = self.move_n_left(row)

        for l in range(self.boardSize):     

            if(l<3):

                if row[l] == row[l+1]:

                    row[l] *= 2
                    self.score += row[l]
                    row[l+1] = 0

                if self.score > self.highscore:

                    f = open("src/logic/highscore.txt", "w")
                    f.write(str(self.score))
                    f.close()

        for l in range(self.boardSize):

            row = self.move_n_left(row)

    def move_left(self, matrix1):

        """   
            Move left funktio siirtää 2048 numerot vasemmalle puolelle
            Jos samat numerot ovat vierekkäin ne yhtyvät yhdeksi numeroksi, joka on x2 alkuperäisistä
            Riville 2|2|0|0 <-- käy siis 4|0|0|0
            Voimme käyttä tätä funktiota muodostamaan kaikki muut siirtofunktiot.

            Args:

            matrix1: Matriisi, jota siirretään 

        """

         # Katsotaan onko vielä mahdollista tehdä liike

        if self.is_game_over() == True:

            # Jos peli on loppu, tyhjennetään matriisi ja nollataan score

            #self.matrix1 = np.zeros((self.boardSize,self.boardSize),dtype="int")
            self.score = 0

        for i in range(self.boardSize):

            row = matrix1[i]

            self.move_row_left(row)

        
        print("")

        print(self.matrix1)
        print(self.score)

    def move_right(self, matrix1):

        reversed_matrix = np.fliplr(matrix1)

        self.move_left(reversed_matrix)

        self.matrix1 = np.fliplr(reversed_matrix)

    def move_up(self, matrix1):

        reversed_matrix = np.transpose(matrix1)

        self.move_left(reversed_matrix)

        self.matrix1 = np.transpose(reversed_matrix)

    def move_down(self, matrix1):

        reversed_matrix = np.transpose(matrix1)

        self.move_right(reversed_matrix)

        self.matrix1 = np.transpose(reversed_matrix)
