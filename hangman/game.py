import random
import os


class Game:
    strikes = 0
    guess = []
    win = False
    end = False

    def __init__(self, max_strike, words):
        self.max_strike = max_strike
        self.words = words

        self.main(self.pick_word(words))

    def censored_word(self):
        letters = []
        for letter in self.word:
            if letter in self.guess:
                letters.append(letter)
            else:
                letters.append("-")
        return "".join(letters)

    def pick_word(self, words):
        return words[random.randint(0, len(words) - 1)].upper()

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def draw(self):
        self.clear()
        print("Strikes {}/{}\nUsed Lettes: {}\nWord: {}\n".format(self.strikes, self.max_strike, ", ".join(self.guess), self.censored_word()))

    def get_letter(self):
        letter = input("Check Letter: ").upper()
        if len(letter) != 1:
            return
        if letter not in self.guess:
            self.guess.append(letter)
            if letter not in self.word:
                self.strikes += 1

    def check_win(self):
        if "-" not in self.censored_word():
            self.win = True
            self.end = True

    def check_lose(self):
        if self.strikes >= self.max_strike:
            self.end = True

    def reset(self):
        self.win = False
        self.end = False
        self.strikes = 0
        self.guess = []

    def main(self, word):
        self.word = word
        self.reset()
        while not self.end:
            self.draw()
            self.get_letter()
            self.check_win()
            self.check_lose()
        self.draw()
        if self.win:
            print("Congratulations, you won the game!")
        else:
            print("Bad luck, wait until next time!")
        print("One more game? (Y/n)")
        if "n" not in input("> ").lower():
            self.main(self.pick_word(self.words))
