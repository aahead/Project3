#syed
import random
import os
import testsave as save

def third_boss_nq(completion):
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
