import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {rows.letter:rows.code for index, rows in alphabets.iterrows()}

# print(phonetic_dict)
user_input = input("Enter a word: ").upper()

output = [phonetic_dict[char] for char in user_input ]

print(output)

    
        
    