from string import ascii_lowercase

def letter_difference(a:str, b:str):
    a_letters = {letter:a.count(letter) for letter in set(a)}
    b_letters = {letter:b.count(letter) for letter in set(a)}
    diff:int = 0
    for letter in ascii_lowercase:
        diff += abs(a_letters.get(letter, 0) - b_letters.get(letter, 0))
    return diff    

def predict(user_input:str):
        letter_differences = [(word, letter_difference(word, user_input)) for word in words]
        def key(value):
             return value[1]
        letter_differences.sort(key=key)
        return letter_differences[:5]

with open("words.txt") as f:
    words:list = f.read().split()

user_input = input()

if user_input in words:
    print(user_input)
    print("This word is in the database.")

print(predict(user_input))