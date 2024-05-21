import random
import logo
print(logo.logo)
print("Welcome to the number guessing game!\nI'm thinking of number between 1 to 100")

def set_difficulty():
    difficulty = input("\nChosse a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 10
    
    return attempts
    

chosen_number = random.randint(1,100)

attempts = set_difficulty()
print(f"You have {attempts} attempts remaining to guess the number")

end = False
while not end and attempts > 0:
    guess = int(input("Make a guess: "))
    
    if guess == chosen_number:
        print(f"You got it! the answer was {guess}")
        end = True
    elif guess > chosen_number:
        print("Too high.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    else:
        print("Too low.\nGuesss again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")

if attempts == 0:
    print("\nSorry you ran out of attempts, You lose")