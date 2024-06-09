# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key' : 'value'}
#     print(a_dictionary['key'])
#     # print(a_dictionary['adddsafa'])
    
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
    
# else:  # This block will run only if the try block runs successfully
#     content = file.read()
#     print(content)

# finally:   # this block will run even if try block runs successfully or not
#     # file.close()
#     # print("the file was closed")
#     raise TypeError("This is an error i made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters")


bmi = weight / height ** 2
print(bmi)