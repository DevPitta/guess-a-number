import PySimpleGUI as sg
from random import randint

guess_image = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/guess-a-number/image/guess_1.png'


class Game:
    def play(self, guess):
        """Run the game"""
        count = 0
        computer = randint(1, 100)
        guess = guess_is_numeric(self, guess)
        while True:
            count += 1
            guess = int(guess)
            if guess == computer:
                sg.popup_no_buttons(f'Congratulations! You guessed the number in {count} guesses!', title='Congratulations', font=12, auto_close=1)
                break
            elif guess < computer:
                print("You kick low, try again!")
                guess = guess_again(self)
                guess = guess_is_numeric(self, guess)
            else:
                print("You kick high, try again!")
                guess = guess_again(self)
                guess = guess_is_numeric(self, guess)


def guess_is_numeric(self, guess):
    """Validates if the guess number is numeric"""
    guess = str(guess)
    while not guess.isnumeric():
        sg.popup('Please enter only numbers!', title='ERROR', font=12, text_color='red')
        guess = guess_again(self)
        if guess.isnumeric():
            break
    return guess


def guess_again(self):
    """Returns to enter a new guess"""
    self.button, self.values = self.window.Read()
    guess = str(self.values['guess'])
    return guess


class PythonScreen(Game):
    def __init__(self):
        # Change color layout
        sg.change_look_and_feel('Dark Blue 3')
        # Layout
        layout = [
            [sg.Text('Guess a number between 1 and 100:', font=14), sg.Input(size=(3, 0), key='guess'), sg.Output(font=14, size=(35, 3))],
            [sg.Button("Play", size=(38, 0), button_color='green')],
            [sg.Image(filename=guess_image)]
        ]
        # Window
        self.window = sg.Window("Guess a Number").layout(layout)

    def Start(self):
        while True:
            # Extract screen data
            self.button, self.values = self.window.Read()
            guess = str(self.values['guess'])
            self.play(guess)
            print('-' * 30)
            play_again = sg.popup_yes_no('Do you want to play again?', title='Play again', font=12)
            if play_again == 'No':
                break
