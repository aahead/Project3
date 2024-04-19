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
        while len(text) > 0:
            username = input("Create a username: ")

            if username in text:
                print("Username in use, please try again")
            else:
                password = input("Create a password: ")
                file.write(f'{username}:{password}\n')
                break


passwords = []
usernames = []
levelpy = []
levelnet = []


global username
def login():
    with open("database2.txt", 'r+') as file:


        no_account = True

        passwords = []
        usernames = []
        levelpy = []
        levelnet = []

        for line in file:

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
                    return (f'{username} successfully logged in\n'
                            f'    Pythonia Level: {levelpy[username_index]}\n"'
                            f"    Netlandia Level: {levelnet[username_index]}")
                    break

                else:
                    print("Password not found")

            else:
                print("Username not found")

create()