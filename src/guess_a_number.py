from random import randint
from colors import FontColors, Styles

fc = FontColors()
s = Styles()


class Game():
    def __init__(self):
        header()
        self.computer = randint(1, 10)
        self.player = input('Guess a number between 1 and 10: ')

    def play(self):
        if not self.player.isnumeric():
            self.player = player_is_numeric(self.player)
        while True:
            self.player = int(self.player)
            if self.player == self.computer:
                print(f'{fc.green}Congratulations, you got it right!{s.end}')
                play_again = str(
                    input('Would you like to play again? [Y/N] ')).strip().upper()
                play_again = play_again_is_Yes_or_No(play_again)
                if play_again == 'N':
                    break
                elif play_again == 'Y':
                    self.computer = randint(1, 10)
                    self.player = input(
                        f'{fc.cyan}Guess a number between 1 and 10: {s.end}')
                    self.player = player_is_numeric(self.player)
            elif self.player < self.computer:
                self.player = input(
                    f'{fc.yellow}You kicked low! Try again: {s.end}')
                self.player = player_is_numeric(self.player)
            else:
                self.player = input(
                    f'{fc.yellow}You kick high! Try again: {s.end}')
                self.player = player_is_numeric(self.player)
        footer()


def player_is_numeric(player):
    while not player.isnumeric():
        player = input(
            f'{fc.red}Invalid input! Type only a number between 1 and 10: {s.end}')
    return player


def play_again_is_Yes_or_No(play_again):
    while play_again not in 'YN':
        play_again = str(
            input(f'{fc.red}Invalid input! Type Y or N: {s.end}')).strip().upper()
        if play_again in 'YN':
            break
    return play_again


def header():
    title = '   GUESS A NUMBER   '
    title_length = len(title)
    print('-' * title_length)
    print(f'{s.bold}{title}{s.end}')
    print('-' * title_length)


def footer():
    title = '   END GAME   '
    title_length = len(title)
    print('-' * title_length)
    print(f'{s.bold}{fc.magenta}{title}{s.end}')
    print('-' * title_length)
