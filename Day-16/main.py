# import turtle
#
# timmy = turtle.Turtle()
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.pencolor("black")
#
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Student Names", ["Priyanshu","Nehal","Pranav","Shoray"])
table.add_column("Student Marks", ["91", "92", "93", "95"])
table.align='l'

print(table)
