
from logic import game

def main():

    game = game.Game()

    game.logic.create_start_pos()

    while True:

        game.run()

if __name__ == "__main__":

    main()

