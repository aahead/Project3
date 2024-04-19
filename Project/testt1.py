def create():
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


def login(username):
    with open("database2.txt", 'r+') as file:


        no_account = True



        for line in file:

            passwords.append(line.split(':')[1])
            usernames.append(line.split(":")[0])
            levelpy.append(line.split(":")[2])
            levelnet.append(line.split(":")[3])

        print(usernames)
        print(passwords)

        while True:

            if username in usernames:
                password = input("Input your password: ")
                usernameindex = usernames.index(username)

                if password == passwords[usernameindex]:
                    print("Logged in")
                    print(f"Pythonia Level: {levelpy[usernameindex]}")
                    print(f"Netlandia Level: {levelnet[usernameindex]}")
                    break

                else:
                    print("Password not found")

            else:
                print("Username not found")

