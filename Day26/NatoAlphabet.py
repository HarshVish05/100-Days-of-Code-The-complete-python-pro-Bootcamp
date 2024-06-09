import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
# challenge for day 30 - add exception handling to the code

phonetic_dict = {rows.letter:rows.code for index, rows in alphabets.iterrows()}

# print(phonetic_dict)

# 1st method

# error = False
# while not error:
#     try:
#         user_input = input("Enter a word: ").upper()

#         output = [phonetic_dict[char] for char in user_input ]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")

#     else:
#         print(output)
#         error  = True

# 2nd method

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[char] for char in user_input ]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output)
       
    
generate_phonetic()
    
        
    