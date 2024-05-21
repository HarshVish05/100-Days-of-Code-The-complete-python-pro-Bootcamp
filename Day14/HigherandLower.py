import random
import game_data
import art


# the second choice will become the first choice in next round even if its not the correct choice
def game_logic(choice1, choice2, user_choice):
    if user_choice == 'A':
        if choice1['follower_count'] > choice2['follower_count']:
            return True
        return False
    else:
        if choice1['follower_count'] < choice2['follower_count']:
            return True
        return False

def choice_taken():
    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}.")
    print(art.versus)
    print(f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}.")

score = 0
end = False
choiceA = random.choice(game_data.data)
choiceB = random.choice(game_data.data)
while not end:
    choice_taken()
    question = input("\nWho has more followers? Type 'A' or 'B': ")
    result = game_logic(choiceA, choiceB, question)

    if result:
        score += 1
        print("You're right, current score: ", score)
        choiceA = choiceB
        choiceB = random.choice(game_data.data)

    else:
        print("Sorry that's wrong. Final score: ", score)
        end = True
