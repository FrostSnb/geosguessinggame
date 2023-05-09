
import random
import json

puzzles = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the tallest mammal?": "Giraffe",
    "What is the smallest country in the world?": "Vatican City",
    "What is the largest ocean?": "Pacific Ocean",
    "What is the smallest planet in our solar system?": "Mercury",
    "What is the largest animal in the world?": "Blue Whale",
    "What is the longest river in the world?": "Nile",
    "What is the highest mountain in the world?": "Mount Everest",
    "What is the closest planet to Earth?": "Venus"
}

def start_new_game():
    print("Welcome to Geo's Guessing Game!!!")
    door_choice = input("Would you like to play? (y or n): ")
    if door_choice == "y":
        print("Ahhh a brave new challenger! A free hint, your answers will be case sensitive.")
        room_generation()
    elif door_choice == "n":
        print("It's too late now! Good luck!")
        room_generation()

def room_check(count):
    if count < 4:
        return room_generation(count)
    else:
        return game_finish()

def room_generation(room_count=0):
    puzzle_attempts = 0
    puzzle_solution = None
    puzzle = random.choice(list(puzzles.keys())) # select a random puzzle from the list
    while puzzle_attempts < 3:
        user_guess = input(puzzle + "\nAnswer: ").strip().title()
        puzzle_solution = puzzles[puzzle].title()
        if user_guess == puzzle_solution:
            print("You solved the puzzle and can move on!")
            del puzzles[puzzle]
            room_count += 1
            room_count = room_check(room_count)
            break
        else:
            puzzle_attempts += 1
            print(f"Wrong! You have {3 - puzzle_attempts} attempts remaining.")
    else:
        print("You have failed.")
        return game_over
    return room_count

def game_finish():
    print("Congratulations! You've completed the game!")
    print("As a reward, you can add your own question to the game.")
    print("Please enter your question and its answer below.")
    new_question = input("Question: ")
    new_answer = input("Answer: ")
    puzzles[new_question] = new_answer
    with open('questions.json', 'w') as f:
        json.dump(puzzles, f, indent=4)
    print("Thank you for your contribution!")
    print("Welcome to the treasure room, you see a shiny chest and feel excited at the prospect of the loot. As you open the chest there is a flash of light and you lose consciousness.")
    return game_over

game_over = True
while game_over:
    with open('questions.json', 'r') as f:
        puzzles = json.load(f)
    play_again = input("Would you like to start a new game? (y/n): ")
    if play_again.lower() == "y":
        start_new_game()
    elif play_again.lower() == "n":
        game_over = False
        print("Thanks for playing!")
    else:
        print