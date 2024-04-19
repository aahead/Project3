import random
import testsave as save

def seccond_boss_py(completion):
    # Define questions and corresponding answers
    questions_and_answers = {
        "What is the output of the following Python code?\nfrom car_functions import calculate_miles_per_gallon\n\ncar_model = 'ABC123'\ndistance_traveled = 300\nfuel_used = 15\n\nmiles_per_gallon = calculate_miles_per_gallon(distance_traveled, fuel_used)\nprint(f'The {car_model} achieved {miles_per_gallon} miles per gallon.')\n\nWhich option do you think is correct?": ["A: The ABC123 achieved 20 miles per gallon.",
                                                                                                    "B: The ABC123 achieved 15 miles per gallon.",
                                                                                                    "C: The ABC123 achieved 25 miles per gallon.",
                                                                                                    "D: The ABC123 achieved 30 miles per gallon.",
                                                                                                    "A"],
        "Consider the following Python code snippet.\ndef process_list(input_list\n\tevens = []\n\todds = []\n\n\tfor num in input_list:\n\t\tif num % 2 == 0:\n\t\t\tevens.append(num)\n\t\telse:\n\t\t\todds.append(num)\n\n\treturn evens, odds\n\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\neven_numbers, odd_numbers = process_list(numbers)\n\nprint('Even numbers:', even_numbers)\nprint('Odd numbers:', odd_numbers)\n\nWhich option do you think is correct?": [
                                                                                                    'A: Even numbers: [2, 4, 6, 8, 10]\n\t   Odd numbers: [1, 3, 5, 7, 9].',
                                                                                                    'B:  Even numbers: [1, 3, 5, 7, 9]\n\t   Odd numbers: [2, 4, 6, 8, 10].',
                                                                                                    'C: Even numbers: [1, 3, 5, 7, 9]\n\t   Odd numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].',
                                                                                                    'D: Even numbers: [2, 4, 6, 8, 10]\n\t   Odd numbers: [2, 4, 6, 8, 10].',
                                                                                                    'B'],
        "Consider the following Python code snippet.\nimport matplotlib.pyplot as plt\n\n# Create a list of character heights (in cm) from Star Wars movies\nheights = [172, 167, 202, 188, 175]\n\n# Create a list of characters' names\ncharacters = ['Luke', 'Leia', 'Vader', 'Han', 'Yoda']\n\n# Plot the heights against the characters\nplt.bar(characters, heights)\nplt.xlabel('Characters')\nplt.ylabel('Height (cm)')\nplt.title('Star Wars Characters Heights')\nplt.show()\n\nWhich option do you think is correct?": [
                                                            "A: It displays a line plot showing the trend of character heights for each character in Star Wars.",
                                                            "B: It displays a bar chart showing the heights of Star Wars characters.",
                                                            "C: It displays a scatter plot showing the relationship between character names and heights.",
                                                            "D: It displays a scatter plot showing the relationship between character names and heights..", "B"],
        "Consider the following Python code snippet.\nimport matplotlib.pyplot as plt\n\ndef plot_movie_ratings(movies, ratings)\n'''\t\n\tPlot movie ratings.\n\n\tParameters:\n\t\tmovies (list): List of movie titles.\n\t\tratings (list): List of corresponding movie ratings.'''\n\t\n\tplt.bar(movies, ratings, color='orange')\n\tplt.xlabel('Movies')\n\tplt.ylabel('Ratings')\n\tplt.title('Movie Ratings')\n\tplt.show()\n\n# List of movie titles\nmovies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction']\n# List of movie ratings\nratings = [9.3, 9.2, 9.0, 8.9]\n\n# Call the function to plot the movie ratings\nplot_movie_ratings(movies, ratings)\n\nWhich option do you think is correct?": [
            "A: It displays a line plot showing the trend of movie ratings over four movies.", "B: It displays a bar chart showing the ratings of four movies.",
            "C: It displays a scatter plot showing the relationship between movie titles and ratings.",
            "D: It displays an error because the data is not properly formatted for plotting.", "B"]
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