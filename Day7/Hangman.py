import random
from words import logo, word_list
from hangmanart import HANGMANPICS
import os 

word_chosen = random.choice(word_list)
word_length = len(word_chosen)

print(logo)
# print("The chosen word is", word_chosen)

display = ['_' for _ in range(word_length)]

lives = len(HANGMANPICS)
death = 0

while '_' in display:
    guess = input('Guess a letter: ').lower()
    
    # this is used to clear the screen after each guess
    os.system('cls')
    
    # checking if the letter is already guessed or not
    if guess in display:
        print(f"You've already guessed the letter {guess}")

    for pos in range(word_length):
        if guess == word_chosen[pos]:
            display[pos] = guess

    if guess not in word_chosen:
        lives -= 1
        print(HANGMANPICS[death])
        death += 1

    if lives == 0:
        print('You Lose, the man died because of your incompetency')
        # print(HANGMANPICS[-1])
        break
    print(display,'\n')


else:
    print('You Won!')
