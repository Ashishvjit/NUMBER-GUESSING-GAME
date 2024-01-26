import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower.")

if __name__ == "__main__":
    guess_the_number()
