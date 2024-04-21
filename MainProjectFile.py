import os
import time
# All the python files
import _1_Boss_Python as firstpy
import _2_Boss_Python as secondpy
import _3_Boss_Python as thirdpy
import _4_Boos_Python as fourthpy
# All the Network files
import test_first_boss_nq as firstnet
from Networking_Bosses import second_boss_nq as secondnet
from Networking_Bosses import third_boss_nq as thirdnet
from Networking_Bosses import NetworkBoss4 as Boss

# Intro For Pythonia
# All Ascii art titles are generated using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20


def main():
    os.system('cls')
    print("Welcome User!")
    username = input("What would you like to go by user? ")
    os.system("cls")
    # Queries the user on what class they would like to study for.
    choice = input("Choose whether you would like to study Python or Networking. p or n: ")
    os.system('cls')
    if choice.lower() == "p":
        print("You awake in a strange forest, before you lies a large double door. The words")
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(2)
        print("\n__          __  _                            _______      _____       _   _                 _   "
              "\n\ \        / / | |                          |__   __|    |  __ \     | | | |               (_)   "
              "\n \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___   | |__) |   _| |_| |__   ___  _ __  _  __ _ "
              "\n  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  |  ___/ | | | __| '_ \ / _ \| '_ \| |/ _` |"
              "\n   \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) | | |   | |_| | |_| | | | (_) | | | | | (_| |"
              "\n    \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/  |_|    \__, |\__|_| |_|\___/|_| |_|_|\__,_|"
              "\n                                                                 __/ |                              "
              "\n                                                                |___/"
              "\nare embossed on its creaking oak front.")
    elif choice.lower() == "n":
        print("You awake in a strange forest, before you lies a large double door. The words", end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(2)
        print("\n __          __  _                            _          _   _      _   _                 _ _  "
              "\n \ \        / / | |                          | |        | \ | |    | | | |               | (_)  "
              "\n  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  \| | ___| |_| | __ _ _ __   __| |_  __ _ "
              "\n   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | . ` |/ _ \ __| |/ _` | '_ \ / _` | |/ _` | "
              "\n    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |\  |  __/ |_| | (_| | | | | (_| | | (_| | "
              "\n     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| \_|\___|\__|_|\__,_|_| |_|\__,_|_|\__,_| ")
        print("are embossed on its creaking oak front.")
    # This will leave time to look at the title and then prompt the user to begin the game.

    time.sleep(3)
    begin = input("Are you ready to Begin? y or n: ")
    # Using a local save file this if statement will greet the user with the username they entered previously.

    # Abram
    # A conditional to make sure the user wants to play
    if begin.lower() == 'y':
        os.system("cls")
        print(f"Good morning {username} I am your conscious Jeff!\nAnd this odd looking fellow running up to you is"
              f"your first enemy, Good Luck!")
        # This calls all the boss files in order and then calls the end function.
        boss1(choice)
        boss2(choice)
        boss3(choice)
        boss4(choice)
        end()
    elif begin.lower() == 'n':
        # This else statement will immediately close the game.
        print("goodbye traveller")
        quit()
    else:
        # If the user types anything other than y or n the game will close.
        print("Alright then see you next time.")
        quit()


# Abram
def boss1(choice):
    if choice.lower() == 'n':
        # This initializes first_boss as an instance of the class NetworkQuiz
        first_boss = firstnet.NetworkQuiz()
        # This calls the first_boss_nq method from the class
        first_boss.first_boss_nq()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the first boss, it's time to meet your second foe!")
        time.sleep(6)
        os.system('cls')
    elif choice.lower() == 'p':
        # This calls the first python quiz function
        firstpy.first_boss_nq()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the first boss, it's time to meet your second foe!")
        time.sleep(6)
        os.system('cls')


# Abram
def boss2(choice):
    if choice.lower() == 'n':
        # This calls the quiz function in the second bosses code
        secondnet()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the second boss, your third opponent awaits.")
        time.sleep(6)
        os.system('cls')
    elif choice.lower() == 'p':
        # This calls the quiz function in the second bosses code
        secondpy.seccond_boss_py()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the second boss, your third opponent awaits.")
        time.sleep(6)
        os.system('cls')


# Abram
def boss3(choice):
    if choice.lower() == 'n':
        # This calls the quiz function in the third bosses code
        thirdnet()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the third boss, the end is near and so is your last battle, GET READY!!!")
        time.sleep(6)
        os.system('cls')

    elif choice.lower() == 'p':
        # This calls the quiz function in the third bosses code
        thirdpy.third_boss_nq()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("You have felled the third boss, the end is near and so is your last battle, GET READY!!!")
        time.sleep(6)
        os.system('cls')


# Abram
def boss4(choice):
    if choice.lower() == 'n':
        # This calls the class for the Fourth bosses quiz code
        fourth_boss = Boss()
        fourth_boss.fourth_boss_nq()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("The journey was hard but you earned your spot among the greatest minds...")
        time.sleep(6)
        os.system('cls')

    elif choice.lower() == 'p':
        # This calls the quiz function in the fourth bosses code
        fourthpy.fourth_boss_nq()
        # These lines will display when you have defeated the boss
        os.system('cls')
        print("The journey was hard but you earned your spot among the greatest minds...")
        time.sleep(6)
        os.system('cls')


# Abram
def end():
    # This statement will check to see if all bosses have been defeated. If they have then the game will be finished.
    print("You have completed the game and finished your Python training.\n"
          "\n  _____                            _         _       _   _  "
          "\n / ____|                          | |       | |     | | (_)  "
          "\n| |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ "
          "\n| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| "
          "\n| |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ "
          "\n \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/ "
          "\n                    __/ | "
          "\n                   |___/                                                   ")


main()
