# Reading all the names
with open('./names/all_names.txt') as names:
    all_names = names.readlines()
    # all_names = names.read()
    # all_names = all_names.split()

new_names = [name.strip() for name in all_names]

# Reading the letter format
with open('./Letter/format.txt') as letter:
    letter_template = letter.read()

# writing the letter
# for name in all_names:
for name in new_names:
    with open(f"../Output/letter_for_{name}.txt", 'w') as letter:
        letter_content = letter_template.format(name = name)
        letter.write(letter_content)

