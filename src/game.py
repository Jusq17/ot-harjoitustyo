
from gamelogic import logic

game = logic()

game.create_start_pos()

print(game.matrix)

#for i in range(10):

    #game.move_left()

    #print(game)

while True:

    l = input("Tee siirtosi")

    if l == "a":

        game.move_left(game.matrix)

    if l == "d":

        game.move_right(game.matrix)

    if l == "w":

        game.move_up(game.matrix)

    if l == "s":

        game.move_down()
