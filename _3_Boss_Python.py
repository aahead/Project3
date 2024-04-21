import random
import os
import time

# Abdelali
def third_boss_nq():
    # Define questions and corresponding answers
    questions_and_answers = {
        "Consider the following Python code snippet:\ntext = 'Python is an amazing programming language.'\n\n# Perform string manipulation\nnew_text = text[:6] + 'was' + text[6:19] + 'excellent' + text[19:]\n\nprint(new_text)": ["A: Python was an amazing programming language.",
                                                                                                    "B: Python is an excellent programming language",
                                                                                                    "C: Python was an amazing programming language.",
                                                                                                    "D: Python is an amazing excellent programming language.",
                                                                                                    "C"],
        "Consider the following Python code snippet.\ntry:\n\twith open('army_data.txt', 'r') as file:\n\t\tdata = file.readlines()\n\t\tcount = 0\n\t\tfor line in data:\n\t\t\tcount += 1\n\t\t\tif count == 3:\n\t\t\t\traise ValueError('Intentional error')\nexcept FileNotFoundError:\n\tprint('File not found.')\nexcept ValueError as e:\n\tprint('An error occurred:', str(e))": [
                                                                                                    'A: "File not found."',
                                                                                                    'B: "An error occurred: Intentional error"',
                                                                                                    'C: "An error occurred: File not found."',
                                                                                                    'D: The code does not produce any output.',
                                                                                                    'B'],
        "Consider the following Python code snippet.\n# Create a dictionary of student names and their corresponding grades\nstudent_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 90}\n\n\n# Calculate the average grade\naverage_grade = sum(student_grades.values()) / len(student_grades)\n\nprint('Average grade:', average_grade)": [
                                                            "A: Average grade: 86.25",
                                                            "B: Average grade: 86.5",
                                                            "C: Average grade: 86.0",
                                                            "D: Average grade: 85.75", "B"],
        "Consider the following Python code snippet.\n# Create a dictionary of students and their respective courses\nstudent_courses = {\n\t'Alice': {'Math', 'Physics', 'Chemistry'},\n\t'Bob': {'Physics', 'Biology', 'Computer Science'},\n\t'Charlie': {'Math', 'Chemistry', 'Computer Science'},\n\t'Diana': {'Physics', 'Chemistry', 'Biology'}\n}\n# Find the students who are enrolled in all three subjects: Math, Physics, and Chemistry\n\nstudents_enrolled = [student for student, courses in student_courses.items() if {'Math', 'Physics', 'Chemistry'}.issubset(courses)]\n\nprint('Students enrolled in Math, Physics, and Chemistry:', students_enrolled)": [
            "A: Students enrolled in Math, Physics, and Chemistry: ['Alice', 'Charlie', 'Diana']", "B: Students enrolled in Math, Physics, and Chemistry: ['Alice', 'Bob', 'Charlie', 'Diana']",
            "C: Students enrolled in Math, Physics, and Chemistry: ['Alice', 'Charlie']",
            "D: Students enrolled in Math, Physics, and Chemistry: ['Alice', 'Diana'].", "A"]
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

