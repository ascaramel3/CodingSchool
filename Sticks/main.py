from os import system

player_1 = [1, 1]
player_2 = [1, 1]
players = [player_1, player_2]

def turn():
    response = input("Attack or split (Type 'A' or 'S')").lower()
    if response == 'a':
        attack()
    elif response == 's':
        split()
    else:
        turn()

def attack():
    atthand = input("Left hand or right hand? (Type 'L' or 'R')").lower()
    defhand = input("Opponent's left or right hand? (Type 'L' or 'R')").lower()
    if not set([atthand, defhand]) <= set('rl'):
        attack()
        return
    index = [int(defhand == 'r')]
    players[1] += players[0][int(atthand == 'r')]
    players[1][[int(defhand == 'r')]] %= 5


def split():
    on_left = input("Amount on left hand:")
    if not on_left.isnumeric():
        split()
    on_left = int(on_left)
    total = sum(players[0])
    if on_left not in range(1, min(total + 1, 5)):
        split()
    result = [on_left, total - on_left]
    if set(result) == set(players[0]):
        turn()
        return
    players[0] = result 

def display():
    system('cls')
    print(player_2, player_1, sep='\n')
    print(f"Player {1 if players[0] is player_1 else 2}'s turn")


while all(map(sum, players)):
    display()
    turn()
    players.reverse()