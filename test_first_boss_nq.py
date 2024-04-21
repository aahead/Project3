import random
import os
import time


# Syed
class NetworkQuiz:

    def __init__(self):
        self.questions_and_answers = {
            "Which network device operates at the Data Link layer (Layer 2) of the OSI model? (module 2)": [
                "a) Hub", "b) Switch", "c) Router", "d) Firewall", "B"],
            "What technology is commonly used for wireless local area networking (WLAN)?  (module 3)": [
                "a) Ethernet", "b) Bluetooth", "c) Wi-Fi", "d) NFC", "C"],
            "Which type of network cable is commonly used for Gigabit Ethernet connections? (module 2)": [
                "a) Coaxial cable", "b) Fiber-optic cable", "c) Cat 5e cable", "d) Cat 6 cable", "D"],
            "What is the primary function of DNS (Domain Name System) in internet communication? (module 1)": [
                "a) Encrypts data transmission for security", "b) Translates domain names to IP addresses",
                "c) Filters malicious traffic from entering the network",
                "d) Manages network routing for optimal performance", "B"]
        }
        self.questions = list(self.questions_and_answers.keys())

        random.shuffle(self.questions)

        self.mistakes_allowed = 2
        self.correct_answers = 0


    def first_boss_nq(self):
        # A while loop ensuring the user cannot exit until the boss is defeated.
        while self.correct_answers != 4:
            # Setting these to the default value ensure that the players counts will restart if they fail the boss
            self.mistakes_allowed = 2
            self.correct_answers = 0
            # Iterate over shuffled questions
            for question in self.questions:
                # Display the question and answer choices
                print(f"\n{question}")
                for option in self.questions_and_answers[question][:4]:
                    print(f"\t{option}")

                # Get user input and validate answer
                user_choice = input("\nType in the letter of the answer choice you chose: ").upper()
                if user_choice == self.questions_and_answers[question][4]:
                    os.system("cls")
                    print("Correct!")
                    self.correct_answers += 1
                else:
                    self.mistakes_allowed -= 1
                    if self.mistakes_allowed > 0:
                        os.system("cls")
                        print(f"Incorrect. You have {self.mistakes_allowed} attempts left.")
                        self.questions.append(question)  # Optionally give another chance by re-adding the question
                    else:
                        print("You died, restart the boss")
                        time.sleep(3)
                        os.system('cls')
                        break
                if self.correct_answers == 4:
                    print("Congratulations you have defeated the boss!")
                    break # Move on to next boss