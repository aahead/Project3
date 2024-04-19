#
# Abdelali Zerrouq
# 04/17/24
# This file creates and logs into accounts so that game progression is saved
#

# Create account function

global username
global password
def create():

    # database2.txt is where all the username and passwords are stored

    with open("database2.txt", 'r+') as file:

        text = file.read()

        #  while the file has anything in it:
        while len(text) >= 0:
            global username
            username = input("Create a username: ")

            #  If the username is in the file, they can't create
            #  a new account with that username
            if username in text:
                print("Username in use, please try again")
            else:

                password = input("Create a password: ")

                # saving the username and password together
                # auto assigning level 0
                file.write(f'{username}:{password}:{0}:{0}\n')
                break


global levelpy
global levelnet
global username_index

def login():
    with open("database2.txt", 'r+') as file:



        global levelpy
        global levelnet
        global username_index

        passwords = []
        usernames = []
        levelpy = []
        levelnet = []

        # iterating through every line in the file
        for line in file:

            # split each line at every ":" to get the :
            # [0] = username
            # [1] = password
            # [2] = pythonia level
            # [3] = network level

            passwords.append(line.split(':')[1])
            usernames.append(line.split(":")[0])
            levelpy.append(line.split(":")[2])
            levelnet.append(line.split(":")[3])


        #while loop until "break"
        while True:

            #two variables global so I can use them throughout the file
            global username
            global password

            #take name and password if username is recognized

            username = input("Input your username: ")
            if username in usernames:
                password = input("Input your password: ")
                username_index = usernames.index(username)

                #check if password matches with the username
                if password == passwords[username_index]:
                    print(f'{username} successfully logged in\n')

                    break


                else:
                    print("Password not found")

            else:
                print("Username not found")

#function to add a level to their py level everytime its called
def pilevel(user,passw,pylevels, netlevels):

    # add a level to python
    pylevels+=1

    # open database2.txt and write the account information formatted
    # so that it can be manipulated
    with open("database2.txt", "w") as file:
        file.write(f'{user}:{passw}:{pylevels}:{netlevels}\n')
    with open("database2.txt", "r") as file:
        for line in file:

            #display levels
            split = line.split(":")
            print(f'    Pythonia Level: {pylevels}')
            print(f"    Netlandia Level: {netlevels}")


#function to add a level to their py level everytime its called

def netlevel(user,passw,pylevels, netlevels):

    with open("database2.txt", "w") as file:
        netlevels+=1

        file.write(f'{user}:{passw}:{pylevels}:{netlevels}\n')
    with open("database2.txt", "r") as file:
        for line in file:
            split = line.split(":")
            print(f'    Pythonia Level: {pylevels}')
            print(f"    Netlandia Level: {netlevels}")


def display(user,passw,pylevels, netlevels):
    with open("database2.txt", "w") as file:
        for line in file:
            print(line)
            print()

