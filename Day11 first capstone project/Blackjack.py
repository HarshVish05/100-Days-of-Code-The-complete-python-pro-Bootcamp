import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# play = input("Do you want to play a game of blackjack, type 'y' or 'n': ")
# if play == "y":
#     print("\nWelcome to BlackJack!")
# else:
#     print("exit")
    
    
player_choice = random.choices(cards, k=2)
computer_choice = random.choices(cards, k=2)
print(f"Your cards: {player_choice}, current score: {sum(player_choice)}")
print(f"Computer's first card: {computer_choice[0]}")