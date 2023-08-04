from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color:")

is_game_on = False

colors = ["red", "green", "orange", "purple","black", "yellow"]
y_position = [-70, -40, -10, 20, 50, 80]

turtle_list = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 215:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Your turtle {user_bet} win!")
            else:
                print(f"You lost!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
