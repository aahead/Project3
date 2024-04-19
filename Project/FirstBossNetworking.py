import random
import testsave as save

def first_boss_nq(completion):
    # Define questions and corresponding answers
    questions_and_answers = {
        "Which network device operates at the Data Link layer (Layer 2) of the OSI model? (module 2)": ["a) Hub",
                                                                                                        "b) Switch",
                                                                                                        "c) Router",
                                                                                                        "d) Firewall",
                                                                                                         "B"],
        "What technology is commonly used for wireless local area networking (WLAN)?  (module 3)": ["a) Ethernet",
                                                                                                    "b) Bluetooth",
                                                                                                    "c) Wi-Fi",
                                                                                                    "d) NFC", "C"],
        "Which type of network cable is commonly used for Gigabit Ethernet connections? (module 2)": [
            "a) Coaxial cable", "b) Fiber-optic cable", "c) Cat 5e cable", "d) Cat 6 cable", "D"],
        "What is the primary function of DNS (Domain Name System) in internet communication? (module 1)": [
            "a) Encrypts data transmission for security", "b) Translates domain names to IP addresses",
            "c) Filters malicious traffic from entering the network",
            "d) Manages network routing for optimal performance", "B"]
    }

    # Create a list of questions and shuffle them
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    mistakes_allowed = 2  # Total mistakes a player can make before they "die"
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