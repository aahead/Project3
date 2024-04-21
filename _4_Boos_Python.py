import random
import os
import time


# Daniel
def fourth_boss_nq():
    # Define questions and corresponding answers
    questions_and_answers = {
        "Consider the following Python code snippet:\nset1 = {1, 2, 3, 4, 5}\nset2 = {4, 5, 6, 7, 8}\n\n# Perform set operations\nresult1 = set1 ^ set2\nresult2 = set1 & set2\n\nprint('Result 1:', result1)\nprint('Result 2:', result2)": ["A: result1 contains the elements {1, 2, 3, 6, 7, 8} and result2 contains the elements {4, 5}.",
                                                                                                    "B: result1 contains the elements {1, 2, 3, 4, 5, 6, 7, 8} and result2 contains the elements {4, 5}.",
                                                                                                    "C: result1 contains the elements {1, 2, 3, 6, 7, 8} and result2 contains the elements {1, 2, 3, 4, 5}.",
                                                                                                    "D: result1 contains the elements {1, 2, 3, 4, 5, 6, 7, 8} and result2 contains the elements {1, 2, 3, 4, 5}.",
                                                                                                    "A"],
        "Consider the following Python code snippet.\ndict1 = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}, 'c': 30}\ndict2 = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}, 'c': 30}\n\n# Perform dictionary operations\nresult1 = dict1 == dict2\nresult2 = dict1 is dict2\n\nprint('Result 1:', result1)\nprint('Result 2:', result2)": [
                                                                                                    'A: result1 is True and result2 is True.',
                                                                                                    'B: result1 is True and result2 is False.',
                                                                                                    'C: result1 is False and result2 is True.',
                                                                                                    'D: result1 is False and result2 is False.',
                                                                                                    'B'],
        "Consider the following Python code snippet.\nclass Vehicle:\n\tdef __init__(self, color):\n\t\tself.color = color\n\nclass Car(Vehicle):\n\tdef __init__(self, color, brand):\n\t\tsuper().__init__(color)\n\t\tself.brand = brand\n\ncar1 = Car('red', 'Toyota')\ncar2 = Car('blue', 'Honda')\n\nprint(car1.color == car2.color)": [
                                                            "A: True",
                                                            "B: False",
                                                            "C: SyntaxError",
                                                            "D: AttributeError", "B"],
        "Consider the following Python code snippet.\nclass Student:\n\tdef __init__(self, name, subjects):\n\t\tself.name = name\n\t\tself.subjects = subjects\n\n# Create instances of Student class\nstudent1 = Student('Alice', {'Math', 'Physics', 'Chemistry'})\nstudent2 = Student('Bob', {'Physics', 'Biology', 'Computer Science'})\nstudent3 = Student('Charlie', {'Math', 'Chemistry', 'Computer Science'})\nstudent4 = Student('Diana', {'Physics', 'Chemistry', 'Biology'})\n\nstudents = [student1, student2, student3, student4]\n\n# Perform set operations on subjects of students\ncommon_subjects = set.intersection(*[student.subjects for student in students])\nunique_subjects = set.union(*[student.subjects for student in students])\n\nprint('Common subjects:', common_subjects)\nprint('Unique subjects:', unique_subjects)": [
            "A: Common subjects: {'Chemistry', 'Physics'}, Unique subjects: {'Math', 'Biology', 'Computer Science', 'Chemistry', 'Physics'}", "B: Common subjects: {'Physics', 'Chemistry'}, Unique subjects: {'Math', 'Biology', 'Computer Science'}",
            "C: Common subjects: {'Physics', 'Chemistry'}, Unique subjects: {'Math', 'Biology', 'Computer Science', 'Chemistry', 'Physics'}",
            "D: Common subjects: {'Chemistry', 'Physics'}, Unique subjects: {'Math', 'Biology', 'Computer Science'}", "B"]
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



