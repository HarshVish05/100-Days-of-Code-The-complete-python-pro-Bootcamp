import os
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def calc(a, b, expression):
    if expression == '+':
        return add(a, b)
    elif expression == '-':
        return sub(a, b)   
    elif expression == '*':
        return mul(a, b)
    else: # expression == '/'
        return div(a, b) 
  
print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      """)
    
end = False
update_first_number = False
while not end:
    if not update_first_number:
        first_number = float(input("What's the first number?: "))
    else:
        first_number = result
        
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the next number?: "))
    
    result = calc(first_number, second_number, operation)

    print(f"{first_number} {operation} {second_number} = {result}")

    continuation = input(f"Type 'y' to continue calculating with {result}, or type 'n' for new calculation and 'e' for exit: ")

    if continuation == 'n':
        update_first_number = False
        os.system('cls')
    elif continuation == 'y':
        update_first_number = True
        first_number = result
    else:
        end = True
    
    
