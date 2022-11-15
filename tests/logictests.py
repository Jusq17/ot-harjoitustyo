#Kaikki itse pelin logikkan liittyvät funktiot ovat tässä tiedostossa
#Esim. 2048 "laudan" "siirto" vasempaan ja oikeaan suuntaan.

import numpy as np
import random

class logic:

    #luodaan pelimatriisi("lauta")

    def __init__(self):
        
        self.matrix = np.matrix('0,0,2,2;2,2,2,2;2,2,2,2;2,2,2,2')
        self.boardSize = 4

    def __str__(self):

        return str(self.matrix)

    def place_n(self):

        print("asetetaan")

        n1 = random.randint(0,3)
        n2 = random.randint(0,3)

        if(self.matrix[n1,n2]!=0):

            self.place_n()
        else:

            self.matrix[n1,n2] = 2

    def create_start_pos(self):

        #kuinka monta numeroa pelin alussa on
        start_numbers_n = 2

        #luodaan indeksit joihin numerot laitetaan ja asetetaan numerot sinne

        for i in range(start_numbers_n):

            self.place_n()


game = logic()


#tehdään testi 10 kertaa, jotta voidaan olla aika varmoja, että numeroille
#joudutaan etsimään uudet paikat.

for i in range(10):

    print(game)

    game.create_start_pos()

    print(game)

    game.matrix = np.matrix('0,0,2,2;2,2,2,2;2,2,2,2;2,2,2,2')
