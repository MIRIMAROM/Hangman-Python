from random import randint


class Game():

    def __init__(self, file_path="C:/Users/Public/miri תכנות/שנה ב/קורס פיתון מרחוק/H.W/משימת סיום פיתון/sentences.txt"):
        self.__sentences = self.__get_sentences(file_path)
        self.__sentence = self.__choose_sentence()
        self.__sentence_to_show = self.__init_sentence_to_show()
        self.__num_of_tryings = 0
        self.__is_winning = False

    def __get_sentences(self, file_path):
        file = open(file_path)
        return [line for line in file]

    def __choose_sentence(self):
        return self.__sentences[randint(0, len(self.__sentences)-2)]

    def __init_sentence_to_show(self):
        str = ""
        for i in range(len(self.__sentence)-1):
            if self.__sentence[i] != ' ':
                str += "_"
            else:
                str += " "
                self.__sentence = self.__sentence[0:i] + '=' + self.__sentence[i + 1:]

        return str

    def __update_sentence_to_show(self, letter):
        if self.__sentence.find(letter) > -1 and letter != "":
            index = self.__sentence.find(letter)
            self.__sentence = self.__sentence[0:index]+'='+self.__sentence[index+1:]
            self.__sentence_to_show = self.__sentence_to_show[0:index]+letter+self.__sentence_to_show[index+1:]

    def check_winning(self):
        return self.__sentence.count('=') == len(self.__sentence)-1

    def __show_page(self):
        print(self.__sentence_to_show)

    def __enter_letter(self):
        return input("enter a letter")

    def start_game(self):
        print("---Man hanging game---")
        print("Guess about class names")
        while not self.check_winning():
            self.__show_page()
            # print(self.__sentence)
            self.__update_sentence_to_show(self.__enter_letter())
            self.__num_of_tryings += 1
        self.__show_page()
        print(f"------- Well done!! - You won !-!-! and your attempts - {self.__num_of_tryings} -------- ")





