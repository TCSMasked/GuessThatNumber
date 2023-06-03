import random
import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the game title
def display_title():
    print("***************************")
    print("*** Guess the Number! ***")
    print("***************************")
    print()

# Function to display the game over screen
def display_game_over(number):
    clear_screen()
    display_title()
    print("GAME OVER")
    print("The number was:", number)
    print()

# Function to display the win screen
def display_win(lives, number):
    clear_screen()
    display_title()
    print("YOU WIN!")
    print("Number of lives used:", lives)
    print("The number was:", number)
    print()
    print("Tweet your victory: https://twitter.com/intent/tweet?text=I%20won%20the%20GuessTheNumber%20game%20in%20{}%20lives!%20Check%20out%20@TCSMasked%27s%20GitHub:%20{}".format(lives, "https://GitHub.com/TCSMasked"))
    print()

# Function to play the game
def play_game(difficulty):
    clear_screen()
    display_title()

    if difficulty == "easy":
        number = random.randint(0, 20)
    elif difficulty == "medium":
        number = random.randint(0, 50)
    else:
        number = random.randint(0, 100)

    lives = 10
    clues = []

    while lives > 0:
        guess = input("Guess the number ({} lives remaining): ".format(lives))
        clear_screen()
        display_title()

        if not guess.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        guess = int(guess)
        lives -= 1
        clues.append(guess)

        if guess == number:
            display_win(10 - lives, number)
            return True
        elif lives == 0:
            display_game_over(number)
            return False
        else:
            print("Incorrect guess! Try again.")
            print("Clues:", clues)
            print()

# Function to start the game
def start_game():
    while True:
        clear_screen()
        display_title()
        difficulty = input("Select difficulty (easy/medium/hard): ").lower()

        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level!")
            continue

        result = play_game(difficulty)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

start_game()