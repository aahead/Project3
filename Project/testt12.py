#
# Abdelali Zerrouq
# 04/17/24
# This file creates and logs into accounts so that game progression is saved
#

# Create account function

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


global username
def login():
    with open("database2.txt", 'r+') as file:

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

        while True:
            global username
            username = input("Input your username: ")
            if username in usernames:
                password = input("Input your password: ")
                username_index = usernames.index(username)


                if password == passwords[username_index]:
                    print(f'{username} successfully logged in\n')
                    print(f'    Pythonia Level: {levelpy[username_index]}\n"')
                    print(f"    Netlandia Level: {levelnet[username_index]}")
                    break

                else:
                    print("Password not found")

            else:
                print("Username not found")

