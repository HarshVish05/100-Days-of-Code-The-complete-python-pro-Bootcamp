print("""
                               I
                                   Y
    |                              T                              |
   .'.                           .' '.                           .'.
  (__ )                        _;-----;_                        (__ )
   |A|                       .':::::    '.                       |A| 
  .===.                     /:::::::      \                     .===.
  |/  |                |   ::::::::        :   |                |/  |
  |/  |      |       ,' ', |:::::::        | ,' ',       |      |/  |
  |/  |     ( )     (:.___)\:::____________/(:.___)     ( )     |/  |
  |===|      H    I  |(_)V__)-------------(__V(_)|  I    H      |===|
  |/  |     |=|   Y_.----|  _______________  |----._Y   |=|     |/  |
  |/  |     |:|   | | __ | [,-------------,] | __ | |   |:|     |/  |
  |/  |     |:|   | |/  \| [|    _.-._    |] |/  \| |   |:|     |/  |
  |===|     |:|   |'||  || [|   /  '::\   |] ||  ||'|   |:|     |===|
  |/  |     |:|   |_||__|| []  |    :::|  [] ||__||_|   |:|     |/  |
  |/  |     |:|   | | __ | []  |    :::|  [] | __ | |   |:|     |/  |
  |/  |     |:|   |.|/  \| []  |    :::|  [] |/  \|.|   |:|     |/  |
  |/  |     |:|   | ||  || []  |     ::|  [] ||  || |   |:|     |/  |
  |/__|_____|:|___| ||__||_[]__|_____::|__[]_||__||_|___|:|_____|/__|
 |/    |-------------------------------------------------------|/    |
 |/    |                                                       |/    |
 |/____|_________________________________________________snd___|/____|

(1997)
      """)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
user_input = input("You're at a cross road. Where do you want to go?\nType 'left' or 'right'\n")
if user_input == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type 'wait' to wait for the boat. Type 'swim' to swim across.\n")
    if choice == 'wait':
        print("You arrive at the island unharmed. There is house with 3 doors")
        color = input("One red, one yellow and one blue. Which colour do you choose?\n")
        if color == 'red':
            print("Burned by fire. Game Over.")
        elif color == 'yellow':
            print("Hurray! You  found the treasure.")
        else:
            print("Eaten by beasts. Game Over.")
    else:
        print("Attacked by Trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
    
    