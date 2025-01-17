from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a colour(red, yellow, green, blue, purple, orange,) : ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() > 230:
            is_race_on = False
            colour = turtle.pencolor()

            if colour == user_bet:
                print(f'You have won ! the {colour} turtle is the winner !')

            else:
                print(f'You have lost ! The {colour} turtle is the winner !')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
