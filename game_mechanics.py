
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print("Welcome to Trivia Trek!!")
    #------------------------
    #------------------------
#---------------------------------------
categories = ['Science', 'History', 'Math', 'Geography']

questions = {
    'Science': [
        {'question': "What is the chemical symbol for water?", 'answer': 'H2O'},
        {'question': "What planet is known as the Red Planet?", 'answer': 'Mars'}
    ],
    'History': [
        {'question': "Who was the first president of the United States?", 'answer': 'George Washington'},
        {'question': "In what year did World War II end?", 'answer': '1945'}
    ],
    'Math': [
        {'question': "What is 5 + 3?", 'answer': '8'},
        {'question': "What is the square root of 16?", 'answer': '4'}
    ],
    'Geography': [
        {'question': "What is the capital of France?", 'answer': 'Paris'},
        {'question': "Which continent is Egypt in?", 'answer': 'Africa'}
    ]
}

def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    print("Choose a category: ")
    for ind, cat in enumerate(categories):
        print(ind, cat)
    choice = int(input("Enter you choice: "))
    return categories[choice -1]
    #------------------------
    
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print(f"Round: {round_number} Score {score}")
    #------------------------
    
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print("Game over. Your final score is {final_score}")
    #------------------------

    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    score = 0
    round_number = 1
    incorrect_answers = 0
    while round_number <= 5:
        print(f"Round: {round_number}")
        category = choose_category(categories)
        questionset = questions[category]
        questiondata = questionset[0]
        print(questiondata["question"])
        player_answer = input("You answer: ")
        correct - validate_answer(player_answer, questiondata["answer"])
        score = update_score(score, correct)
        display_score(score, round_number)
    
    #------------------------

    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    return player_answer.strip().lower() == correct_answer.strip().lower()
    #------------------------
    
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if correct:
        return score + 10
    else:
        return score
    #------------------------
    
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return round_number + 1
    #------------------------

    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    return incorrect_answers >= 3
    #------------------------
    
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    choice = input("Do you want to go again? ")
    if choice == "yes" or "Yes":
        run_game_rounds(categories)
    else:
        print("Byeeee!")
    #------------------------
    
    #------------------------

#---------------------------------------
