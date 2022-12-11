
import pygame as pygame
from logic import gamelogic

class UI():

    def __init__(self):

        pygame.init()

        #self.clock = pygame.time.Clock()

        #self.matrix = gamelogic.matrix

        #self.logic = gamelogic.Logic()

        self.size = self.width, self.height = 800, 800
        self.black = (0, 0, 0)

        self.gainsboro = (220,220,220)
        self.silver = (192,192,192)
        self.gray = (128,128,128)
        self.orange = (244,164,96)
        self.darkorange = (255,150,0)
        self.orangered = (255,90,0)
        self.red = (255,50,0)
        self.yellow = (255,255,0)
        self.yellow2 = (255,240,0)

        self.rows = 4
        self.cols = 4
        
        self.block_size = 150

        self.one_digit = pygame.font.Font('freesansbold.ttf', 80)
        self.two_digit = pygame.font.Font('freesansbold.ttf', 67)
        self.three_digit = pygame.font.Font('freesansbold.ttf', 52)

        #self.screen = pygame.display.set_mode(self.size)

    def draw_matrix(self, matrix, screen):

        for row in range(0,4):

            #print(row)

            for col in range(0,4):

                x = self.block_size * row + 8 * row + 90
                y = self.block_size * col + 8 * col + 125

                #print(matrix)

                #m = matrix()

                number = str(matrix[col][row])

                #print(number)

                # Värit laatikoihin

                if int(number) == 2:

                    pygame.draw.rect(screen, self.gainsboro, (x,y,self.block_size,self.block_size))

                elif int(number) == 4:

                    pygame.draw.rect(screen, self.silver, (x,y,self.block_size,self.block_size))

                elif int(number) == 8:

                    pygame.draw.rect(screen, self.orange, (x,y,self.block_size,self.block_size))

                elif int(number) == 16:

                    pygame.draw.rect(screen, self.darkorange, (x,y,self.block_size,self.block_size))

                elif int(number) == 32:

                    pygame.draw.rect(screen, self.orangered, (x,y,self.block_size,self.block_size))

                elif int(number) == 64:

                    pygame.draw.rect(screen, self.red, (x,y,self.block_size,self.block_size))

                elif int(number) == 128:

                    pygame.draw.rect(screen, self.yellow, (x,y,self.block_size,self.block_size))

                else:

                    pygame.draw.rect(screen, self.gray, (x,y,self.block_size,self.block_size))

                if number != "0":

                    if int(number) < 10:

                        screen.blit(self.one_digit.render(number, True, (0,0,0)), (x + self.block_size/4, y + self.block_size/4))

                    elif 10 < int(number) < 1000:

                        screen.blit(self.two_digit.render(number, True, (0,0,0)), (x + self.block_size/4, y + self.block_size/4))

                    else:

                        screen.blit(self.three_digit.render(number, True, (0,0,0)), (x + self.block_size/4, y + self.block_size/4))


    def drawUI(self, screen, matrix, score):

        screen.fill(self.black)

        self.draw_matrix(matrix, screen)

        #self.score = str(self.logic.score)

        #score = gamelogic.Logic().Score()

        screen.blit(self.three_digit.render("Score: " + str(score), True, (255,255,255)),(50, 50))

        #screen.fill(self.black)

        #pygame.draw.rect(screen,(255,255,255),(0,0,200,200))

        #print("mo")

#ui = UI()

#ui.drawUI()

#while True:

    #ui.drawUI()

