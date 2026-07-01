from requests import get
from random import choice
from os import system

url = 'https://raw.githubusercontent.com/Xethron/Hangman/refs/heads/master/words.txt'
words = get(url).content.decode().split()[:-3]
secret_word = choice(words)

hp = lambda: 6 - len(guessed_letters - set(secret_word))

def display():
    print(f'HP: {hp()}')
    print(*guessed_letters)
    print(build_blanks())

guessed_letters: set = set()
build_blanks = lambda: ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])

while hp() > 0 and guessed_letters != set(secret_word):
    system('cls')
    display()
    guess: str = input('Guess a letter: ')
    if len(guess) != 1:
        continue
    guessed_letters.add(guess)
    
if hp() == 0:
    system('cls')
    display()

    print(f"\nThe word was {secret_word}.")
    print("Better luck next time >:)")
else:
    print("Good job for guessing the word! :)")
    
