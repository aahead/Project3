#syed
import random
import os
import testsave as save

def second_boss_nq(completion):
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

    mistakes_allowed = 2
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