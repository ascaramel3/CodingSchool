from requests import get
from random import choice
from os import system
from termcolor import colored

url = 'https://gist.githubusercontent.com/shmookey/b28e342e1b1756c4700f42f17102c2ff/raw/ed4c33a168027aa1e448c579c8383fe20a3a6225/WORDS'

words:list[str] = get(url).text.split()
words = [word.upper() for word in words if len(word) == 5]

word = choice(words)
assert len(word) == 5

guesses:list[str] = []

def display():
    system('cls')
    print("Wordle")

    for guess in guesses:
        highlight(guess)
        print()

def highlight(guess) -> None:
    letters = list(word)
    for i, letter in enumerate(guess):
        if letter == word[i]:
            color = 'green'
        elif letter in word:
            color = 'yellow'
        else:
            color = 'light_grey'
        print(colored(letter, color), end='')
       

 

while len(guesses) < 6 and word not in guesses:
    display()
    guess = input('\nGuess a 5-character word: ').upper()
    if len(guess) != 5 or not guess.isalpha or guess not in words:
        continue
    guesses.append(guess)
display()
print(f'The word was: {word}')