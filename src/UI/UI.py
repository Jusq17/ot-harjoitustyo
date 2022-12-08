
import pygame as pygame
from logic import gamelogic

class UI():

    def __init__(self):

        pygame.init()

        #self.clock = pygame.time.Clock()

        #self.matrix = gamelogic.matrix

        self.size = self.width, self.height = 800, 800
        self.black = (0, 0, 0)

        self.rows = 4
        self.cols = 4
        
        self.block_size = 190

        self.pointsFont = pygame.font.Font('freesansbold.ttf', 80)

        #self.screen = pygame.display.set_mode(self.size)

    def draw_matrix(self, matrix, screen):

        for row in range(0,4):

            #print(row)

            for col in range(0,4):

                x = self.block_size * row + 8 * row + 8
                y = self.block_size * col + 8 * col + 8

                #print(matrix)

                #m = matrix()

                number = str(matrix[col][row])

                #print(number)

                pygame.draw.rect(screen,(255,255,255),(x,y,self.block_size,self.block_size))

                if number != "0":
                    screen.blit(self.pointsFont.render(number, True, (0,0,0)), (x + self.block_size/4, y + self.block_size/4))


    def drawUI(self, screen, matrix):

        #screen.fill(self.black)

        self.draw_matrix(matrix, screen)

        #pygame.draw.rect(screen,(255,255,255),(0,0,200,200))

        #print("mo")

#ui = UI()

#ui.drawUI()

#while True:

    #ui.drawUI()

