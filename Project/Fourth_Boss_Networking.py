#syed
import random
import os
import testsave as save

def fourth_boss_nq(completion):
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

    #2uestions and corresponding answers for unbeatable
    questions_and_answers2 = {"Which of the following is a characteristic of a collision domain?": [
        "a) It consists of devices connected to a hub.", "b) It consists of devices connected to a switch.",
        "c) It is bounded by routers.", "d) It is associated with broadcast traffic.", "A"],

        "Which routing protocol typically uses link-state advertisements (LSAs) to communicate network topology changes?": [
            "a) RIP (Routing Information Protocol)", "b) OSPF (Open Shortest Path First)", "c) BGP (Border Gateway Protocol)"
            ,"d) EIGRP (Enhanced Interior Gateway Routing Protocol)", "B"],

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

    def answer_checking(qanda):
        # Create a list of questions and shuffle them
        questions = list(qanda.keys())
        random.shuffle(questions)

        mistakes_allowed = 1
        correct_answers = 0
        # Iterate over shuffled questions
        for question in questions:
            # Display the question and answer choices
            print(f"\n{question}")
            for option in questions_and_answers[question][:4]:
                print(f"\t{option}")

            # Get user input and validate answer
            user_choice = input("\nType in the letter of the answer choice you chose: ").upper()
            if user_choice == questions_and_answers[question][4]:
                print("Correct!")
                correct_answers += 1
            else:
                mistakes_allowed -= 1
                if mistakes_allowed > 0:
                    print(f"Incorrect. You have {mistakes_allowed} attempts left.")
                    questions.append(question)  # Optionally give another chance by re-adding the question
                else:
                    print("You died, restart the boss")
                    break  # Exit the loop if no more mistakes are allowed
            if correct_answers == 4:
                print("Congratulations you have defeated the boss!")
                if completion < 2:
                    completion += 1
                    save.pilevel(save.username, save.password, save.levelpy, save.levelnet)
                    print(save.display(save.username, save.password, save.levelpy, save.levelnet))
                else:
                    pass
                break



    print("Hardness Levels Available: \n\t-Hard (1)\n\t-Unbeatable (2)\n\t-1337 (3)")
    #tests if the input is a number and if not error given and repompted
    while True:
        try:
            hardness = int(input("\nhow hard would you like the final boss to be? Press the number next to the hardness to continue: "))
            break
        except:
            print("Can only type numbers")
    Flag = True
    while Flag == True: #checks if 1 2 or 3 is typed in for the hardness or reprompted
        try:
            os.system("cls")
            if hardness == 1: #hardness level hard
                answer_checking(questions_and_answers1)
                Flag = False
            elif hardness == 2: #hardness level unbeatable
                answer_checking(questions_and_answers2) #calls the function that randomizes questions and checks for correct answer
                Flag = False
            elif hardness == 3: #hardness level 1337
                print("\nWhats the best way to solve a problem?") #question
                Leet_answer = input("Answer: ").lower()
                if Leet_answer == "scroll down" or Leet_answer == "1337": #answer
                    print("your teacher is proud of you")
                else:
                    print("you suck")
                Flag = False

            else:
                print("You can only choose numbers between 1 and 3")
        except ValueError:
            print("you can only type in Letters")

