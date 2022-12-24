
import configparser

class file_mnger():

    def __init__(self):

        #def read_config():
        
        file = open("data/highscore.txt", "r")
        content = file.readlines()
        file.close()

        self.highscore = content[0]

    def return_hs(self):

        file = open("data/highscore.txt", "r")
        content = file.readlines()
        file.close()

        self.highscore = content[0]

        return self.highscore

    def write_hs(self, score):

        f = open("data/highscore.txt", "w")
        f.write(str(score))
        f.close()

    def return_colors(self):

        config = configparser.ConfigParser()
        config.read("data/colors.ini")

        color_section = config["colors"]
        color_names = [color for color in color_section]

        colors = []

        for color in color_names:

            color_tuple = tuple(map(int,color_section[color].split(', ')))

            colors.append(color_tuple)

        return colors