import Menu

menu = Menu.MENU
resources = Menu.resources


def make_coffee(user_choice, money):
    if user_choice == 'report':
        print(resources)
    elif user_choice == 'espresso':
        if menu['espresso']['ingredients']['water'] < resources['water'] and menu['espresso']['ingredients']['coffee'] < resources['coffee']:
            resources['water'] -= menu['espresso']['ingredients']['water']
            resources['coffee'] -= menu['espresso']['ingredients']['coffee']
            check_cost(money,user_choice)
        else:
            print("Sorry we don't have the resources left")
            
            
    elif user_choice == 'latte':
        if menu['latte']['ingredients']['water'] < resources['water'] and menu['latte']['ingredients']['coffee'] < resources['coffee'] and menu['latte']['ingredients']['milk'] < resources['milk']:
            resources['water'] -= menu['latte']['ingredients']['water']
            resources['coffee'] -= menu['latte']['ingredients']['coffee']
            check_cost(money,user_choice)
        else:
            print("Sorry we don't have the resources left")
            
            
    elif user_choice == 'cappuccino':
        if menu['cappuccino']['ingredients']['water'] < resources['water'] and menu['cappuccino']['ingredients']['coffee'] < resources['coffee'] and menu['cappuccino']['ingredients']['milk'] < resources['milk']:
            resources['water'] -= menu['cappuccino']['ingredients']['water']
            resources['coffee'] -= menu['cappuccino']['ingredients']['coffee']
            check_cost(money,user_choice)
        else:
            print("Sorry we don't have the resources left")

  # check this function it is not working as expected          
def check_cost(money,choice):
    if choice == 'espresso' and menu['espresso']['cost'] < money:
        print("Your espresso is ready")
    elif choice == 'latte' and menu['latte']['cost'] < money:
        print("Your latte is ready")
    elif choice == 'cappuccino' and menu['cappuccino']['cost'] < money:
        print("Your cappuccino is ready")
    else:
        print("Insufficient money")

end = False
while not end:

    choice = input(
        "\nYou can type 'end' to end the coffee maker.\nHere we offer 'espresso', 'latte' and 'cappuccino'\nWhat would you like? ")
    
    money = int(input("How much money do you have? "))
    if choice == 'end':
        print(resources)
        end = True

    make_coffee(choice, money)
