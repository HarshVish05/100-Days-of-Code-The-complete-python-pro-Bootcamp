import random

choices  = ['rock','paper','scissor']

print('Welcome to Rock Paper and Scissor game!')
name = input("Hi player, what's your name? ")
user_choice = input('Enter your choice\n').lower()

comp_choice = random.choice(choices)
print("comp choice is ",comp_choice)

if user_choice == comp_choice:
    print("It's a tie")
    
elif (user_choice== 'rock' and comp_choice=='scissor'):
    print(f"Hurray {name} wins!")
elif(user_choice == 'rock' and comp_choice == 'paper'):
    print(f"Sorry {name}, you lose this time.")
    
elif (user_choice== 'scissor' and comp_choice=='rock'):
    print(f"Sorry {name}, you lose this time.")
elif(user_choice == 'scissor' and comp_choice == 'paper'):
    print(f"Hurray {name} wins!")
    
elif (user_choice== 'paper' and comp_choice=='scissor'):
    print(f"Sorry {name}, you lose this time.")
elif(user_choice == 'paper' and comp_choice == 'rock'):
    print(f"Hurray {name} wins!")
else:
    print("invalid input")
