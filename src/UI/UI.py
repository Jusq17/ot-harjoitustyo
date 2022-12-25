
import pygame as pygame
from file_management import file_manager


class UI():

    """
        Luokka, joka vastaa Käyttöliittymän ja grafiikan piirtämisestä näytölle.

        Attributes:

            colors: numerollisten laatikoiden värit
            black: musta väri
            gray: harmaa väri
            rows: laudan rivien määrä
            cols: laudan sarakkeiden määrä
            block_size: laudan laatikoiden koko
            one_digit: fontti yksinumeroisille
            two_digit: fontti kaksinumeroisille
            three_digit: fontti kolmenumeroisille ja isommille
            score_font: fontti scorea varten
    """

    def __init__(self):

        self.file_manager = file_manager.file_mnger()

        pygame.init()

        self.colors = self.file_manager.return_colors()

        self.black = (0, 0, 0)
        self.gray = (128, 128, 128)

        self.rows = 4
        self.cols = 4

        self.block_size = 150

        self.one_digit = pygame.font.Font('freesansbold.ttf', 80)
        self.two_digit = pygame.font.Font('freesansbold.ttf', 67)
        self.three_digit = pygame.font.Font('freesansbold.ttf', 59)
        self.score_font = pygame.font.Font('freesansbold.ttf', 34)

    def draw_matrix(self, matrix, screen):
        """
            Metodi, joka vastaa pelimatrsiin piirtämisestä.

            Args:

                matrix: matriisi, josta tieto saadaan piirtoa varten
                screen: pygame ikkuna, johon grafiikat piirretään

        """

        for row in range(0, 4):

            for col in range(0, 4):

                x = self.block_size * row + 8 * row + 90
                y = self.block_size * col + 8 * col + 80

                number = str(matrix[col][row])

                # Värit laatikoihin

                if int(number) == 2:

                    pygame.draw.rect(screen, self.colors[0],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 4:

                    pygame.draw.rect(screen, self.colors[1],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 8:

                    pygame.draw.rect(screen, self.colors[2],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 16:

                    pygame.draw.rect(screen, self.colors[3],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 32:

                    pygame.draw.rect(screen, self.colors[4],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 64:

                    pygame.draw.rect(screen, self.colors[5],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 128:

                    pygame.draw.rect(screen, self.colors[6],
                                     (x, y, self.block_size, self.block_size))

                elif int(number) > 128:

                    pygame.draw.rect(screen, self.colors[7],
                                     (x, y, self.block_size, self.block_size))

                else:

                    pygame.draw.rect(screen, self.gray,
                                     (x, y, self.block_size, self.block_size))

                if number != "0":

                    if int(number) < 10:

                        screen.blit(self.one_digit.render(
                            number, True, (0, 0, 0)), (x + self.block_size/4, y + self.block_size/4))

                    elif 10 < int(number) < 100:

                        screen.blit(self.two_digit.render(
                            number, True, (0, 0, 0)), (x + self.block_size/4, y + self.block_size/4))

                    elif 100 < int(number) < 1000:

                        screen.blit(self.three_digit.render(
                            number, True, (0, 0, 0)), (x + self.block_size/7, y + self.block_size/4))

                    else:

                        screen.blit(self.three_digit.render(
                            number, True, (0, 0, 0)), (x + self.block_size/18, y + self.block_size/4))

    def draw_menu_UI(self, screen):
        """
            Metodi, joka vastaa start-menun piirtämisestä

            Args:

                screen: pygame ikkuna, johon grafiikat piirretään

        """

        screen.fill(self.black)

        screen.blit(self.one_digit.render(
            "2048", True, (self.colors[3])), (300, 80))
        screen.blit(self.three_digit.render(
            "Press Enter to start!", True, (255, 255, 255)), (100, 300))
        screen.blit(self.score_font.render(
            "Use the arrow keys to move the numbers!", True, (self.colors[6])), (50, 500))

    def draw_main_UI(self, screen, matrix, score):
        """
            Metodi, joka vastaa koko käyttöliittymästä

            Args:

                matrix: matriisi, josta tieto saadaan piirtoa varten
                screen: pygame ikkuna, johon grafiikat piirretään
                score: score, joka piirretään

        """

        highscore = self.file_manager.return_hs()

        screen.fill(self.black)
        self.draw_matrix(matrix, screen)

        screen.blit(self.score_font.render(
            "Score: " + str(score), True, (255, 255, 255)), (50, 20))
        screen.blit(self.score_font.render("Highscore: " +
                    highscore, True, (255, 255, 255)), (400, 20))
        screen.blit(self.three_digit.render(
            "Press R to retry", True, (255, 255, 255)), (180, 720))
