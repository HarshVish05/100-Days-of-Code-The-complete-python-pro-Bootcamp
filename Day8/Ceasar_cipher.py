def encrypt(plain_text, shift_amount):  # eg - hello  output = mjqqt  shift = 5
    encrypted_text = ""
    for char in plain_text:
        pos = alphabet.index(char)
        new_pos = (pos + shift_amount) % 26
        
        encrypted_text += alphabet[new_pos]
    return encrypted_text

def decrypt(cipher_text, shift_amount):
    return encrypt(cipher_text, shift_amount * -1)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Taking necessary inputs from the user


end = False
while not end:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt and 'end' to end the program\n")
    
    if direction == 'end':
        print ("\nEnding program...")
        end = True
        
    elif direction == 'encode':
        text = input("Enter the text to encode: ").lower()
        shift = int(input("Type the shift number: "))
        print(f"The encoded text is {encrypt(text, shift)} \n")
        
    elif direction == 'decode':
        encode_text = input("Enter the text to decode: ").lower()
        shift = int(input("Type the shift number: "))
        print(f"The decoded text is {decrypt(encode_text, shift)} \n")
    
    else:
        print("\nInvalid Input! Please type according to the instruction given. ")
        
        






