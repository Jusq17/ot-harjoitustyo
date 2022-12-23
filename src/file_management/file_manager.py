
class file_mnger():

    def __init__(self):
        
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