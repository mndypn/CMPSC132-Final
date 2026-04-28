import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    game_over = False

    while not game_over:
        user_input = input("Guess a number: ")
        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed it in {attempts} attempts!")
                game_over = True
            elif guess < number:
                print("Too low, guess a higher number")
            else:
                print("Too high, guess a lower number")
        
        else:
            print ("Invalid input. Please enter an integer")


number_guessing_game()