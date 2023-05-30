import random

slot_machine = [["*", "*", "*"],
                ["*", "*", "*"],
                ["*", "*", "*"]]

ICONS = ['A', 'B', 'C', 'X', 'Y', 'Z', '1', '2', '3', '7', '@', '#', '&']

coins = 100


def menu():
    print('''
    1. Spin machine
    2. Show win conditions
    ''')
    choice = int(input("What would you want to do? "))
    if choice == 1:
        bet_amt = int(input("How much do you want to bet? "))
        play_game(bet_amt)
    elif choice == 2:
        show_win_conditions()
    elif choice == 0:
        return 'exit'
    else:
        print("Invalid choice")

    return ''


def get_row():
    return [random.choice(ICONS), random.choice(ICONS), random.choice(ICONS)]


def spin_machine():
    slot_machine[0] = get_row()
    slot_machine[1] = get_row()
    slot_machine[2] = get_row()
    print(slot_machine)


def show_win_conditions():
    print('''
    1. Three 7s (5x)
    2. Numbers in a sequence (3.2x)
    3. Alphabets in a sequence (2.8x)
    4. Three different symbols (2.3x)
    5. Any 3 symbols (1.5x) 
    6. Any 3 numbers (1.3s)
    7. Any 3 letters (1.2x)
    ''')


def check_wins(bet_amt):
    global coins
    line_row = slot_machine[1]
    val1, val2, val3 = line_row
    is_win = [False, 0]

    symbol_list = ['@', '#', '&']
    num_list = ["1", "2", "3", "7"]
    alpha_list = ['A', 'B', 'C', 'X', 'Y', 'Z']

    if val1 == 7 and val2 == 7 and val3 == 7:
        coins += bet_amt * 5
        is_win = [True, 5]
    elif val1 == '1' and val2 == '2' and val3 == "3":
        coins += bet_amt * 3.2
        is_win = [True, 3.2]
    elif val1 == 'A' and val2 == 'B' and val3 == "C" or \
            val1 == 'X' and val2 == 'Y' and val3 == "Z":
        coins += bet_amt * 2.8
        is_win = [True, 2.8]
    elif val1 in symbol_list and val2 in symbol_list and val3 in symbol_list:
        coins += bet_amt * 1.5
        is_win = [True, 1.5]
    elif val1 in num_list and val2 in num_list and val3 in num_list:
        coins += bet_amt * 1.3
        is_win = [True, 1.3]
    elif val1 in alpha_list and val2 in alpha_list and val3 in alpha_list:
        coins += bet_amt * 1.2
        is_win = [True, 1.2]
    else:
        coins -= bet_amt

    if is_win[0] == True:
        print(f"YOU WON!!!!! {bet_amt * is_win[1]} ({is_win[1]}x)")


def display_slot():
    print(f'{slot_machine[0]}\n{slot_machine[1]}\n{slot_machine[2]}')


def play_game(bet_amt):
    spin_machine()
    display_slot()
    check_wins(bet_amt)
    print(f"You now have ${coins}")


while True:
    print(f"current coins ${coins}")
    quit_menu = menu()
    if quit_menu:
        break
