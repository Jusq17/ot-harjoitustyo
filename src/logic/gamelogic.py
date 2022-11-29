#Kaikki itse pelin logikkan liittyvät funktiot ovat tässä tiedostossa
#Esim. 2048 "laudan" "siirto" vasempaan ja oikeaan suuntaan.

import numpy as np
import random

class Logic:

    #luodaan pelimatriisi("lauta")

    def __init__(self):
        
        self.boardSize = 4
        self.matrix1 = np.zeros((self.boardSize,self.boardSize),dtype="int")

        # gameState = 0: Peli ei ole alkanut, gameState = 1: Peli on käynnissä 
        # gameState = 2: Peli loppu epäonnistuneesti, gameState = 3: Peli loppu ja 2048 saavutettu.

        self.gameState = 0

    def __str__(self):

        return str(self.matrix)

    def matrix(self):

        return self.matrix1

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

        #if(self.matrix1[n1,n2]!=0):

            #self.place_n()
        #else:

            #self.matrix1[n1,n2] = 2

    def create_start_pos(self):

        #kuinka monta numeroa pelin alussa on
        start_numbers_n = 2

        #luodaan indeksit joihin numerot laitetaan ja asetetaan numerot sinne

        for i in range(start_numbers_n):

            n1 = random.randint(0,3)
            n2 = random.randint(0,3)

            self.matrix1[n1,n2] = 2

            #self.place_n()

    # Move left funktio siirtää 2048 numerot vasemmalle puolelle
    # Jos samat numerot ovat vierekkäin ne yhtyvät yhdeksi numeroksi, joka on x2 alkuperäisistä
    # Riville 2|2|0|0 <-- käy siis 4|0|0|0
    # Voimme käyttä tätä funktiota muodostamaan kaikki muut siirtofunktiot. 

    def move_n_left(self, row):

        for l in range(self.boardSize-1):

            #print(row[l])

            if row[l] == 0 and row[l+1] != 0:

                row[l+1], row[l] = row[l], row[l+1]

        return row

    def move_row_left(self, row):

        #print(row)

        for l in range(self.boardSize):

            row = self.move_n_left(row)

        for l in range(self.boardSize):

            #print(row[l])

            if(l<3):

                if row[l] == row[l+1]:

                    row[l] *= 2
                    row[l+1] = 0

        for l in range(self.boardSize):

            row = self.move_n_left(row)

    def move_left(self, matrix1):

        for i in range(self.boardSize):

            row = matrix1[i]

            self.move_row_left(row)
        
        print("")

        #self.place_n()

        print(self.matrix1)

    def move_right(self, matrix1):

        reversed_matrix = np.fliplr(matrix1)

        self.move_left(reversed_matrix)

        self.matrix1 = np.fliplr(reversed_matrix)

        #print(self.matrix)

    def move_up(self, matrix1):

        reversed_matrix = np.transpose(matrix1)

        self.move_left(reversed_matrix)

        #self.matrix = reversed_matrix

        self.matrix1 = np.transpose(reversed_matrix)

        #print(self.matrix)

    def move_down(self, matrix1):

        reversed_matrix = np.transpose(matrix1)

        self.move_right(reversed_matrix)

        #self.matrix = reversed_matrix

        self.matrix1 = np.transpose(reversed_matrix)

        #print(self.matrix)

#game = logic()

#game.create_start_pos()

#print(game.matrix)

#for i in range(10):

    #game.move_left()

    #print(game)

#while True:

    #l = input("Tee siirtosi")

    #if l == "a":

        #game.move_left(game.matrix)

    #if l == "d":

        #game.move_right(game.matrix)

    #if l == "w":

        #game.move_up()

    #if l == "s":

        #game.move_down()
