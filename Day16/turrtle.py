# from turtle import Turtle,Screen

# timmy = Turtle()

# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color('aqua')
# timmy.forward(100)

# print(my_screen.canvheight)
# my_screen.exitonclick()

# print(timmy)


# prettytable module is used to creatd tables in ascii format
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",['Pikachu','squirtle','Blastoise','Bulbasaur','charmander'])
table.add_column("Type",['Electric','water','water','grass','Fire'])
table.align = 'l'  # changing the alignment of the table to left
print(table)