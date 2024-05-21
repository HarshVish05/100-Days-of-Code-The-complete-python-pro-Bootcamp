import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','^','&','*','(',')','{','}','|','?','>','<','[',']',':',';','"',',','.','/','~','_','+','=','-']

print("Welcome to pypassword generator!")
no_of_letters = int(
    input("How many letters would you like your password to be?\n"))
no_of_symbols = int(
    input("How many symbols would you like in your password?\n"))
no_of_numbers = int(
    input("How many numbers would you like in your password?\n"))

# Easy level - sequence wise 

# password = ''

# for i in range(0,no_of_letters):
#     password += random.choice(letters)
    
# for i in range(0,no_of_symbols):
#     password += random.choice(symbols)

# for i in range(0,no_of_numbers):
#     password += random.choice(numbers)
    
# print(f"Your password generated is {password}")

# Hard level - Jumbled up
password = []

for i in range(0,no_of_letters):
    password += random.choice(letters)
    
for i in range(0,no_of_symbols):
    password += random.choice(symbols)

for i in range(0,no_of_numbers):
    password += random.choice(numbers)
    
random.shuffle(password)
    
print(f"Your password generated is {''.join(password)}")
