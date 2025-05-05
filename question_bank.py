#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
         ("What is the atomic number of oxygen?", "8"),
        ("Who is the father of modern physics?", "Albert Einstein"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What is the chemical formula for methane?", "CH4"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("What is the powerhouse of the cell?", "Mitochondria"),
        ("What is the chemical symbol for gold?", "Au"),
        ("Who developed the theory of evolution?", "Charles Darwin"),
        ("What is the chemical symbol for salt?", "NaCl"),
    ],
    "History": [
        ("Who was the first president of the United States?", "George Washington"),
        ("In which year did World War II end?", "1945"),
        ("Who was the first emperor of China?", "Qin Shi Huang"),
        ("Which country did the Titanic sail from?", "England"),
        ("Who discovered America?", "Christopher Columbus"),
        ("What year did the French Revolution begin?", "1789"),
        ("Who was the leader of the Soviet Union during World War II?", "Joseph Stalin"),
        ("Which battle was fought in 1066 in England?", "Battle of Hastings"),
        ("Which country was formerly known as Persia?", "Iran"),
        ("Who was the first man to step on the moon?", "Neil Armstrong"),
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which is the largest ocean in the world?", "Pacific Ocean"),
        ("Which continent is the Sahara Desert located in?", "Africa"),
        ("What is the longest river in the world?", "Nile"),
        ("Which country has the largest population?", "China"),
        ("What is the smallest country in the world?", "Vatican City"),
        ("In which country is the Great Barrier Reef?", "Australia"),
        ("What is the highest mountain in the world?", "Mount Everest"),
        ("Which country is known as the Land of the Rising Sun?", "Japan"),
        ("Which country has the longest coastline?", "Canada"),
    
    

    ],
}

hints = {
    "Science": [
        "It’s the element with atomic number 8.",
        "This person developed the theory of relativity.",
        "It’s the temperature at which water boils.",
        "It’s a colorless, odorless gas found in many fuels.",
        "It’s the 4th planet from the Sun.",
        "This organelle is inside the cell and responsible for producing energy.",
        "It’s a yellow metal that has been used for coins and jewelry for centuries.",
        "This person is known for his theory of evolution.",
        "It’s a compound made of sodium and chlorine.",
    ],
    "History": [
        "First president of the USA.",
        "It ended in 1945.",
        "He was the first emperor of China.",
        "The Titanic sailed from this English port.",
        "This explorer sailed in 1492.",
        "It started in 1789.",
        "He was the leader of the Soviet Union during WWII.",
        "It was fought in 1066 in England.",
        "This country changed its name in 1935.",
        "He stepped on the moon in 1969.",
    ],
    "Geography": [
        "It’s known as the City of Light.",
        "It’s the world’s largest ocean.",
        "It’s a vast desert located in Africa.",
        "It’s the longest river in the world.",
        "It’s the most populous country in the world.",
        "This city is the world’s smallest country.",
        "It’s located off the coast of Queensland, Australia.",
        "It’s located in the Himalayas and stands at 8,848 meters.",
        "It’s an island nation in East Asia.",
        "It has the longest coastline of any country.",
    

    ],
    
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    if category in questions and questions[category]:
        return random.choice(questions[category])
    else:
        return None
    #------------------------
    
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    return player_answer.strip().lower() == correct_answer.strip().lower()
    #------------------------
    
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        questions[category] = [q for q in questions[category] if q[0] != question]
    #------------------------
    
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print("Question:", question)
    return input("Your answer: ")
    #------------------------
    
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    if category in questions and category in hints:
        try:
            index = [q[0] for q in questions[category]].index(question)
            return hints[category][index]
        except ValueError:
            return "No hint available."
    return "No hint available."
    #------------------------
    
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print(f"The correct answer was: {correct_answer}")
    #------------------------

#---------------------------------------