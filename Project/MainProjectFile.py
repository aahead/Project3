import os
import time
import testsave as save
import testmap as pymap
import testmapnet as netmap
# These are all the different completed maps for the python map
import py1testmap as pl1map
import py2testmap as pl2map
import py3testmap as pl3map
import py4testmap as pl4map
# These are all the different completed maps for the network map
import net1testmap as nl1map
import net2testmap as nl2map
import net3testmap as nl3map
import net4testmap as nl4map
# These are the bosses for Networking
import FirstBossNetworking as nboss1
import Second_Boss_Networking as nboss2
import Thrid_Boss_Networking as nboss3
import Fourth_Boss_Networking as nboss4
# These are the bosses for Python
import _1_Boss_Python as pboss1
import _2_Boss_Python as pboss2
import _3_Boss_Python as pboss3
import _4_Boos_Python as pboss4
# Intro For Pythonia
# All Ascii art titles are generated using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20


def main():
    # Questions the user and asks if they want to log in to a previous account.
    os.system("cls")
    account = input("Do you already have a saved game? y or n: ")
    if account == 'y':
        save.login()
    elif account == 'n':
        save.create()

    completion = 0
    print(completion)
    os.system("cls")
    # Queries the user on what class they would like to study for.
    choice = input("Choose whether you would like to study Python or Networking. p or n: ")
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

    if begin.lower() == 'y':
        os.system("cls")
        print(f"Good morning {save.username} I am your conscious Jeff!")
        map_(completion, choice)
    elif begin.lower() == 'n':
        # This else statement will immediately close the game.
        print("goodbye traveller")
        quit()
    else:
        print("Alright then see you next time.")
        quit()

    return map_(completion, choice)


def boss1(completion, choice):
    if choice.lower() == 'n':
        nboss1.first_boss_nq(completion)
        if completion < 1:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            elif restart.lower() == 'n':
                map_(completion=0, choice='n')
        elif completion >= 1:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='n')

    elif choice.lower() == 'p':
        pboss1.first_boss_nq(completion)
        if completion < 1:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            if restart.lower() == 'n':
                map_(completion=0, choice='p')
        elif completion >= 1:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='p')


def boss2(completion, choice):
    if choice.lower() == 'n':
        nboss2.second_boss_nq(completion)
        if completion < 2:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            elif restart.lower() == 'n':
                map_(completion=0, choice='n')
        elif completion >= 2:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='n')

    elif choice.lower() == 'p':
        pboss2.seccond_boss_py(completion)
        if completion < 2:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            if restart.lower() == 'n':
                map_(completion=0, choice='p')
        elif completion >= 2:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='p')


def boss3(completion, choice):
    if choice.lower() == 'n':
        nboss3.third_boss_nq(completion)
        if completion < 3:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            elif restart.lower() == 'n':
                map_(completion=0, choice='n')
        elif completion >= 3:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='n')

    elif choice.lower() == 'p':
        pboss3.third_boss_nq(completion)
        if completion < 3:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            if restart.lower() == 'n':
                map_(completion=0, choice='p')
        elif completion >= 3:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='p')


def boss4(completion, choice):
    if choice.lower() == 'n':
        nboss4.fourth_boss_nq(completion)
        if completion < 3:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            elif restart.lower() == 'n':
                map_(completion=0, choice='n')
        elif completion >= 3:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                boss2(completion, choice='n')
            if move_on.lower() == 'n':
                map_(completion, 'n')

    elif choice.lower() == 'p':
        pboss4.fourth_boss_nq(completion)
        if completion < 3:
            restart = input("Would You like to restart? y or n: ")
            while restart.lower() != 'n' or restart.lower() != 'y':
                print("Answer must be y or n")
                restart = input("Would You like to restart? y or n: ")
            if restart.lower() == 'y':
                boss1(completion=0, choice='n')
            if restart.lower() == 'n':
                map_(completion=0, choice='p')
        elif completion >= 3:
            move_on = input("Would you like to move on to the next boss or go to your map? y for boss, n for map: ")
            while move_on.lower() != 'n' or move_on.lower() != 'y':
                print("Answer must be y or n")
                move_on = input("Would you like to move on to the end or go to your map? y for boss, n for map: ")
            if move_on.lower() == 'y':
                end(completion)
            if move_on.lower() == 'n':
                map_(completion, 'p')


def map_(completion, choice):
    # This is the map code for the Pythonia portion of the game
    if completion == 0 and choice.lower() == 'p':
        pymap.map_python()
        print("This is your current map, you have defeated zero bosses.")
        # This variable asks the user to enter a place on the map they would like to travel to.
        map_choice = input("Would you like to travel to the first boss? y or n: ")
        while map_choice.lower() != 'y' or map_choice.lower() != 'n':
            if map_choice.lower() == 'y':
                os.system('cls')
                boss1(completion, choice)
            elif map_choice.lower() == 'n':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 1 and choice.lower() == 'p':
        pl1map.map_python()
        print("This is your current map, you have defeated one boss.")
        map_choice = input("Which boss would you like to travel to? 1, 2, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 2 and choice.lower() == 'p':
        pl2map.map_python()
        print("This is your current map, you have defeated two bosses.")
        map_choice = input("Which boss would you like to travel to? 1, 2, 3, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 3 and choice.lower() == 'p':
        pl3map.map_python()
        print("This is your current map, you have defeated three bosses.")
        map_choice = input("Which boss would you like to travel to? 1, 2, 3, 4, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice == '4':
                os.system('cls')
                boss4(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 4 and choice.lower() == 'p':
        pl4map.map_python()
        print("This is your current map, you have defeated all bosses.")
        map_choice = input("Which boss would you like to travel to? 1,2, 3, 4, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice == '4':
                os.system('cls')
                boss4(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()

    # This is the map code for the Netlandia portion of the game
    if completion == 0 and choice.lower() == 'n':
        netmap.map_network()
        print("This is your current map, you have completed zero bosses.")
        map_choice = input("Would you like to travel to the first boss? y or n: ")
        while map_choice.lower() != 'y' or map_choice.lower() != 'n':
            if map_choice.lower() == 'y':
                os.system('cls')
                boss1(completion)
            elif map_choice.lower() == 'n':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 1 and choice.lower() == 'n':
        nl1map.map_network()
        print("This is your current map, you have defeated one boss.")
        map_choice = input("Which boss would you like to travel to? 1, 2, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 2 and choice.lower() == 'n':
        nl2map.map_network()
        print("This is your current map, you have defeated two bosses.")
        map_choice = input("Which boss would you like to travel to? 1, 2, 3, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 3 and choice.lower() == 'n':
        nl3map.map_network()
        print("This is your current map, you have defeated three bosses.")
        map_choice = input("Which boss would you like to travel to? 1, 2, 3, 4, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice == '4':
                os.system('cls')
                boss4(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()
    elif completion == 4 and choice.lower() == 'n':
        nl4map.map_network()
        print("This is your current map, you have defeated all bosses.")
        map_choice = input("Which boss would you like to travel to? 1,2, 3, 4, or quit: q: ")
        while map_choice != '1' or map_choice != '2' or map_choice == '3' or map_choice.lower() == 'q':
            if map_choice == '1':
                os.system('cls')
                boss1(completion)
            elif map_choice == '2':
                os.system('cls')
                boss2(completion)
            elif map_choice == '3':
                os.system('cls')
                boss3(completion)
            elif map_choice == '4':
                os.system('cls')
                boss4(completion)
            elif map_choice.lower() == 'q':
                print("Very well traveller goodbye for now.")
                quit()


def end(completion):
    # This statement will check to see if all bosses have been defeated. If they have then the game will be finished.
    if completion == 4:
        print("You have completed the game and finished your Python training."
           "   _____                            _         _       _   _  "               
             "/ ____|                          | |       | |     | | (_)  "              
            "| |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ "
            "| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| "
            "| |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ "
            " \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/ "
         "                       __/ | "
          "                     |___/                                                   ")
    else:
        print("You are not finished yet.")


main()
