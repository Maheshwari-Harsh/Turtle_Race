from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Enter the color of the turtle you want to bet on: ")

colors = ["red", "blue", "orange", "green", "pink", "black"]

turtles = []
y_position = [0, 30, -30, 60, -60, 90]
race_is_on = False

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won. The {winning_color} turtle won the race.")
            else:
                print(f"You lose. The {winning_color} turtle won the race.")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
