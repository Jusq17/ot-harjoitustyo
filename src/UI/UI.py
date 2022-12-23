
import pygame as pygame
from logic import file_manager


class UI():

    def __init__(self):

        self.file_manager = file_manager.file_mnger()

        pygame.init()

        self.size = self.width, self.height = 800, 800
        self.black = (0, 0, 0)

        self.gainsboro = (220, 220, 220)
        self.silver = (192, 192, 192)
        self.gray = (128, 128, 128)
        self.orange = (244, 164, 96)
        self.darkorange = (255, 150, 0)
        self.orangered = (255, 90, 0)
        self.red = (255, 50, 0)
        self.yellow = (255, 255, 0)
        self.yellow2 = (255, 240, 0)

        self.rows = 4
        self.cols = 4

        self.block_size = 150

        self.one_digit = pygame.font.Font('freesansbold.ttf', 80)
        self.two_digit = pygame.font.Font('freesansbold.ttf', 67)
        self.three_digit = pygame.font.Font('freesansbold.ttf', 59)
        self.score_font = pygame.font.Font('freesansbold.ttf', 34)

    def draw_matrix(self, matrix, screen):

        for row in range(0, 4):

            for col in range(0, 4):

                x = self.block_size * row + 8 * row + 90
                y = self.block_size * col + 8 * col + 80

                number = str(matrix[col][row])

                # Värit laatikoihin

                if int(number) == 2:

                    pygame.draw.rect(screen, self.gainsboro,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 4:

                    pygame.draw.rect(screen, self.silver,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 8:

                    pygame.draw.rect(screen, self.orange,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 16:

                    pygame.draw.rect(screen, self.darkorange,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 32:

                    pygame.draw.rect(screen, self.orangered,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 64:

                    pygame.draw.rect(screen, self.red,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) == 128:

                    pygame.draw.rect(screen, self.yellow,
                                     (x, y, self.block_size, self.block_size))

                elif int(number) > 128:

                    pygame.draw.rect(screen, self.yellow2,
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

                    else:

                        screen.blit(self.three_digit.render(
                            number, True, (0, 0, 0)), (x + self.block_size/7, y + self.block_size/4))

    def draw_main_UI(self, screen, matrix, score):

        highscore = self.file_manager.return_hs()

        screen.fill(self.black)
        self.draw_matrix(matrix, screen)

        screen.blit(self.score_font.render(
            "Score: " + str(score), True, (255, 255, 255)), (50, 20))
        screen.blit(self.score_font.render("Highscore: " +
                    highscore, True, (255, 255, 255)), (400, 20))
        screen.blit(self.three_digit.render(
            "Press R to retry", True, (255, 255, 255)), (180, 720))

    def draw_menu_UI(self, screen):

        screen.fill(self.black)

        screen.blit(self.one_digit.render(
            "2048", True, (self.orange)), (300, 80))
        screen.blit(self.three_digit.render(
            "Press Enter to start!", True, (255, 255, 255)), (100, 300))
        screen.blit(self.score_font.render(
            "Use the arrow keys to move the numbers!", True, (self.yellow)), (50, 500))

# ui = UI()

# ui.drawUI()

# while True:

    # ui.drawUI()
