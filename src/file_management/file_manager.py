
import configparser


class file_mnger():

    """
        Luokka, joka hoitaa kaiken tiedostonhallintaan liittyvän.

        Attributes:

            highscore_path: polku highscore.txt tiedostoon

    """

    def __init__(self):

        self.highscore_path = "data/highscore.txt"

    def return_hs(self):
        """
            Metodi, joka palauttaa highscoren

            args: none

        """

        with open(self.highscore_path, "r") as f:

            content = f.readlines()
            f.close()

            highscore = content[0]

        return highscore

    def write_hs(self, score):
        """

            Metodi, joka kirjoitaa uuden highscoren tiedostoon.

            args: none

        """

        with open("data/highscore.txt", "w") as f:

            f.write(str(score))
            f.close()

    def return_colors(self):
        """
            Metodi, joka palauttaa colors.ini tiedoston värit käytettävässä muodossa.

            args: none

        """

        config = configparser.ConfigParser()
        config.read("data/colors.ini")

        color_section = config["colors"]
        color_names = list(color_section)

        colors = []

        for color in color_names:

            color_tuple = tuple(map(int, color_section[color].split(', ')))

            colors.append(color_tuple)

        return colors
