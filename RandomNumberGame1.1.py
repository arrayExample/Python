def display_menu():
    print("\n===========Main Menu===========")
    print("1. Play Game.")
    print("2. Directions.")
    print("9. Exit Program.\n")
    return int(input("Selection > "))


def play_game():
    import random
    attempt_counter = 0
    magical_number = random.randint(1, 32)
    while attempt_counter <= 7:
        try:
            user_input = int(input("Selection (1 -> 32): "))
        except ValueError:
            print("You did not enter a number.\nTry again.\n\nYou have attempted", + attempt_counter, "of 7 attempts.")
            continue
        attempt_counter = attempt_counter + 1
        if user_input != magical_number:
            if user_input < magical_number:
                print("Too low.\nYou have attempted", + attempt_counter, "of 7 attempts.")
            if user_input > magical_number:
                print("Too High.\nYou have attempted", + attempt_counter, "of 7 attempts.")
        if user_input == magical_number:
            print("Congrats! You guessed the number correctly.")
            break


def directions():
    print("To start the game simply enter 1 into the Main Menu.")
    print("Once the game is started guess a randomly picked number between 1 and 32.")
    print("The computer will give you hints as to if the number you picked is too high or too low.")
    print("WARNING! You only have 7 attempts!")


print("========Guess a Number!========")
menu_selection = display_menu()
while menu_selection != 9:
    if menu_selection == 1:
        play_game()
    elif menu_selection == 2:
        directions()
    menu_selelection = display_menu()
print("Exiting Program...")
