import turtle
import turtle as t
import random
tim = t.Turtle()

tim.pensize(8)
directions = [0, 90, 180, 270]
tim.speed("fastest")

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_need = (r, g, b)
    return random_color_need


for _ in range(200):
    tim.color(random_color())
    tim.forward(45)
    tim.setheading(random.choice(directions))


t.Screen()
t.exitonclick()
