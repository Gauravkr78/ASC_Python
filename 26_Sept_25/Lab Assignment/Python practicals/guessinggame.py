import random  # Import random module for generating random numbers

def guessing_game():
    """
    A number guessing game between 1 and 100.
    Player has 7 attempts to guess the number.
    """
    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0  # to count how many guesses taken
    max_attempts = 7  # total attempts allowed

    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    # Loop for each attempt
    while attempts < max_attempts:
        try:
            # Take user guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return  # end game on correct guess

        except ValueError:
            print("Please enter a valid number!")  # handle non-integer inputs

    # If all attempts are used and not guessed
    print(f"\n Game over! The number was {secret_number}.")

# Call the function
guessing_game()
