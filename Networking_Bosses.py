import random
import os
import time






# Abdelali
def second_boss_nq():
    # Define questions and corresponding answers
    questions_and_answers = {
        "What is the primary purpose of a router in a home network? (module 4) ": ["a) To connect devices within the same network ",
                                                                                                        "b) To connect the home network to the internet ",
                                                                                                        "c) To provide power to connected devices ",
                                                                                                        "d) To amplify Wi-Fi signals",
                                                                                                        "B"],
        "Which network protocol is commonly used for file sharing in a home network? (module 4))": ["a) HTTP",
                                                                                                    "b) FTP",
                                                                                                    "c) TCP",
                                                                                                    "d) IP", "B"],
        "In the OSI model, which layer is responsible for establishing, maintaining, and terminating connections between nodes in a network? (module 5) ": [
            "a) Physical Layer", "b) Data Link Layer", "c) Network Layer", "d) Transport Layer", "D"],
        "What is the primary purpose of network media in a communication system? (module 6) )": [
            "a) To establish connections between devices", "b) To transmit data between devices ",
            "c) To provide power to network devices",
            "d) To encrypt data for secure transmission", "B"]
    }

    # Create a list of questions and shuffle them
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    correct_answers = 0
    # A while loop ensuring the user cannot exit until the boss is defeated.
    while correct_answers != 4:
        # Setting these to the default value ensure that the players counts will restart if they fail the boss
        correct_answers = 0
        # Total mistakes a player can make before they "die"
        mistakes_allowed = 2
        # Iterate over shuffled questions
        for question in questions:
            # Display the question and answer choices
            print(f"\n{question}")
            for option in questions_and_answers[question][:4]:
                print(f"\t{option}")

            # Get user input and validate answer
            user_choice = input("\nType in the letter of the answer choice you chose: ").upper()
            if user_choice == questions_and_answers[question][4]:
                os.system('cls')
                print("Correct!")
                correct_answers += 1
            else:
                mistakes_allowed -= 1
                if mistakes_allowed > 0:
                    os.system('cls')
                    print(f"Incorrect. You have {mistakes_allowed} attempts left.")
                    questions.append(question)  # Optionally give another chance by re-adding the question
                else:
                    print("You died, restart the boss")
                    time.sleep(3)
                    os.system('cls')
                    break
            if correct_answers == 4:
                print("Congratulations you have defeated the boss!")
                break


# Syed
def third_boss_nq():
    # Define questions and corresponding answers
    questions_and_answers = {
        "What is the primary function of the Access Layer in a network architecture? (Module 7) ": ["a) Routing packets between different subnets",
                                                                                                        "b) Providing high-speed connectivity to end devices",
                                                                                                        "c) Implementing security measures at the network perimeter",
                                                                                                        "d) Managing network traffic congestion",
                                                                                                        "B"],
        "Which of the following technologies is commonly used in the Access Layer to enhance? (Module 7) ": ["a) Virtual Private Networks (VPNs)",
                                                                                                    "b) Intrusion Detection Systems (IDS)",
                                                                                                    "c) VLANs (Virtual Local Area Networks)",
                                                                                                    "d) Quality of Service (QoS) protocols", "C"],
        "Which version of the Internet Protocol (IP) is most widely used today? (Module 8)": [
            "a) IPv4", "b) IPv10", "c) IPv5", "d) IPv6", "A"],
        "Which subnet mask is commonly used in IPv4 to create separate network segments? (Module 9)": [
            "a) 255.255.0.0", "b) 255.255.255.0",
            "c) 255.0.0.0",
            "d) 255.255.255.255", "C"]
    }

    # Create a list of questions and shuffle them
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    correct_answers = 0
    # A while loop ensuring the user cannot exit until the boss is defeated.
    while correct_answers != 4:
        # Setting these to the default value ensure that the players counts will restart if they fail the boss
        correct_answers = 0
        # Total mistakes a player can make before they "die"
        mistakes_allowed = 2
        # Iterate over shuffled questions
        for question in questions:
            # Display the question and answer choices
            print(f"\n{question}")
            for option in questions_and_answers[question][:4]:
                print(f"\t{option}")

            # Get user input and validate answer
            user_choice = input("\nType in the letter of the answer choice you chose: ").upper()
            if user_choice == questions_and_answers[question][4]:
                os.system('cls')
                print("Correct!")
                correct_answers += 1
            else:
                mistakes_allowed -= 1
                # If you run out of allotted mistakes
                if mistakes_allowed > 0:
                    os.system('cls')
                    print(f"Incorrect. You have {mistakes_allowed} attempts left.")
                    questions.append(question)  # Optionally give another chance by re-adding the question
                else:
                    print("You died, restart the boss")
                    time.sleep(3)
                    os.system('cls')
                    break
            # If you get the correct amount of right answers.
            if correct_answers == 4:
                print("Congratulations you have defeated the boss!")
                break

# Syed
class Boss:
    def answer_checking(self, qanda):
        # Create a list of questions and shuffle them
        questions = list(qanda.keys())
        random.shuffle(questions)

        correct_answers = 0
        # A while loop ensuring the user cannot exit until the boss is defeated.
        while correct_answers != 4:
            # Setting these to the default value ensure that the players counts will restart if they fail the boss
            correct_answers = 0
            # Total mistakes a player can make before they "die"
            mistakes_allowed = 2
            # Iterate over shuffled questions
            for question in questions:
                # Display the question and answer choices
                print(f"\n{question}")
                for option in qanda[question][:4]:
                    print(f"\t{option}")

                # Get user input and validate answer
                user_choice = input("\nType in the letter of the answer choice you chose: ").upper()
                if user_choice == qanda[question][4]:
                    os.system('cls')
                    print("Correct!")
                    correct_answers += 1
                else:
                    mistakes_allowed -= 1
                    # If you run out of allotted mistakes
                    if mistakes_allowed > 0:
                        os.system('cls')
                        print(f"Incorrect. You have {mistakes_allowed} attempts left.")
                        questions.append(question)  # Optionally give another chance by re-adding the question
                    else:
                        print("You died, restart the boss")
                        time.sleep(3)
                        os.system('cls')
                        break
                # If you get the correct amount of right answers.
                if correct_answers == 4:
                    print("Congratulations you have defeated the boss!")
                    break

class NetworkBoss4(Boss):
    def fourth_boss_nq(self):
        # questions and corresponding answers for hard
        questions_and_answers1 = {"In a TCP three-way handshake, what is the purpose of the SYN and ACK flags?":
                                      ["a) SYN: Synchronize sequence numbers; ACK: Acknowledge receipt of data",
                                       "b) SYN: Acknowledge receipt of data; ACK: Synchronize sequence numbers",
                                       "c) SYN: Establish a connection; ACK: Close the connection",
                                       "d) SYN: Request to terminate the connection; ACK: Confirm termination of the connection",
                                       "A"],

                                  "Which of the following routing protocols is classified as a distance-vector routing protocol?": [
                                      "a) OSPF (Open Shortest Path First)", "b) BGP (Border Gateway Protocol)",
                                      "c) RIP (Routing Information Protocol)",
                                      "d) EIGRP (Enhanced Interior Gateway Routing Protocol)", "C"],

                                  "What is the main difference between collision and broadcast domains in networking?": [
                                      "a) Collision domains are bounded by switches; broadcast domains are bounded by routers.",
                                      "b) Collision domains are bounded by routers; broadcast domains are bounded by switches.",
                                      "c) Collision domains are associated with VLANs; broadcast domains are associated with subnets.",
                                      "d) Collision domains are associated with multicast traffic; broadcast domains are associated with unicast traffic.",
                                      "A"],

                                  "Which of the following statements accurately describes the purpose of ARP (Address Resolution Protocol) in a TCP/IP network?": [
                                      "a) ARP resolves IPv6 addresses to MAC addresses.",
                                      "b) ARP resolves MAC addresses to IPv4 addresses.",
                                      "c) ARP resolves domain names to IP addresses.",
                                      "d) ARP resolves IP addresses to port numbers.", "B"]}

        # questions and corresponding answers for unbeatable
        questions_and_answers2 = {"Which of the following is a characteristic of a collision domain?": [
            "a) It consists of devices connected to a hub.", "b) It consists of devices connected to a switch.",
            "c) It is bounded by routers.", "d) It is associated with broadcast traffic.", "A"],

            "Which routing protocol typically uses link-state advertisements (LSAs) to communicate network topology changes?": [
                "a) RIP (Routing Information Protocol)", "b) OSPF (Open Shortest Path First)", "c) BGP (Border Gateway Protocol)"
                , "d) EIGRP (Enhanced Interior Gateway Routing Protocol)", "B"],

            "In the context of network address translation (NAT), what is the purpose of dynamic NAT?": [
                "a) To translate multiple private IP addresses to a single public IP address",
                "b) To translate a single private IP address to multiple public IP addresses",
                "c) To statically map private IP addresses to public IP addresses",
                "d) To dynamically allocate public IP addresses from a pool for outgoing traffic", "D"],

            "What is the primary advantage of using a stateful firewall over a stateless firewall?": [
                "a) Stateful firewalls are more efficient at handling high traffic volumes.",
                "b) Stateful firewalls can inspect and track the state of active connections.",
                "c) Stateful firewalls are easier to configure and manage.",
                "d) Stateful firewalls provide better compatibility with legacy protocols.", "B"]
        }

        print("Hardness Levels Available: \n\t-Hard (1)\n\t-Unbeatable (2)\n\t-1337 (3)")
        # tests if the input is a number and if not error given and reprompted
        while True:
            try:
                hardness = int(input("\nHow hard would you like the final boss to be? Press the number next to the hardness to continue: "))
                break
            except:
                print("Can only type numbers")
        Flag = True
        while Flag:
            try:
                os.system("cls")
                if hardness == 1:  # hardness level hard
                    self.answer_checking(questions_and_answers1)
                    Flag = False
                elif hardness == 2:  # hardness level unbeatable
                    self.answer_checking(questions_and_answers2)  # calls the function that randomizes questions and checks for correct answer
                    Flag = False
                elif hardness == 3:  # hardness level 1337
                    print("\nWhat's the best way to solve a problem?")  # question
                    Leet_answer = input("Answer: ").lower()
                    if Leet_answer == "scroll down" or Leet_answer == "1337":  # answer
                        print("Your teacher is proud of you")
                    else:
                        print("You suck")
                    Flag = False

                else:
                    print("You can only choose numbers between 1 and 3")
            except ValueError:
                print("You can only type in numbers")

# fourth_boss = NetworkBoss4()
# fourth_boss.fourth_boss_nq()
