
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# with the help of with keyword
# reading the file
with open('my_file.txt') as file:
    contents = file.read()
    # print(contents)


# writing -  this mode will erase all previous text and write a new one.
# with open("my_file.txt", mode= 'w') as file:
#     file.write("writing this part.")

# this method will create new file if it doesnt exist but the mode should be write 
with open("../new_file.txt", mode= 'w') as file:
    file.write("writing this part to check path.")
    
# writing - this mode will append the new contents after previous one
# with open("my_file.txt", mode= 'a') as file:
#     file.write("\nwriting this part.")