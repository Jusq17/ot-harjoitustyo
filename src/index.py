
import game.game_main as game

def main():

    main_game = game.Game()

    main_game.logic.create_start_pos()

    while True:

        main_game.run()


if __name__ == "__main__":

    main()
