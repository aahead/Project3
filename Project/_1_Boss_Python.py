import random


def first_boss_nq(completion):
    # Define questions and corresponding answers
    questions_and_answers = {
        "Which of the following statements is NOT true regarding the input() function in Python?": ["A: The input() function always returns a string.",
                                                                                                    "B: input() function can accept an optional prompt as an argument.",
                                                                                                    "C: input() function evaluates the user input as Python code.",
                                                                                                    "D: input() function throws an error if the user enters a non-numeric value when expecting numeric input.",
                                                                                                    "C"],
        "What will the following code snippet output?\ntotal = 0)\n   for i in range(1, 6):\n       total += i\n       print(total)": [
                                                                                                    'A: 10',
                                                                                                    'B: 15 ',
                                                                                                    'C: 5',
                                                                                                    'D: 20',
                                                                                                    'B'],
        "What is the purpose of the 'elif' keyword in Python?": [
                                                            "A: To execute a block of code if the condition of the preceding 'if' statement is true.",
                                                            "B: To define an alternate condition to be checked if the condition of the preceding 'if' statement is false.",
                                                            "C: To terminate the execution of the program if the condition of the preceding 'if' statement is false.",
                                                            "D: To repeat a block of code until a certain condition is met.", "B"],
        "What will be the output of the following Python code?\ntotal = 0\nfor i in range(1, 21):\n    if i % 2 == 0:''\n        total += i\nprint('The sum of even numbers between 1 and 20 is: ', total)": [
            "A: 100", "B: 90",
            "C: 110",
            "D: 120", "C"]
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
            if completion < 1:
                completion += 1
            else:
                pass
            break