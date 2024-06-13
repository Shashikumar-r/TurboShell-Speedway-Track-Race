from turtle import Turtle,Screen
from random import randint
color_list = ["yellow", "blue", "orange", "red", "maroon",  "magenta"]

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Turtle Race",prompt="in which color turtle you will bid").lower()


all_turtle = []
for loop in range(5):
    y_position = [-100, -60, -20, 20, 60]
    y_axis = y_position[loop]
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_axis)
    new_turtle.fillcolor(color_list[loop])
    all_turtle.append(new_turtle)
is_on = True
while is_on:
    for turtle in all_turtle:
        turtle_forward = turtle.forward(randint(1,10))
        if turtle.xcor() > 230:
            is_on = False
            if user_input == turtle.fillcolor():
                print(f"Congratulation you won the match, the winning turtle is {turtle.fillcolor()} turtle")
            else:
                print(f"Iam sorry you lost the match, the winning turtle is {turtle.fillcolor()} turtle")





screen.exitonclick()



