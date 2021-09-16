import turtle
from random import random

R = 66
while True:
    turtle.forward(R * random())
    if random() > 0.5:
        turtle.left(random() * 360)
    else: 
        turtle.right(random()* 360)
