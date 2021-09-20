from font_config import *
from turtle import Vec2D as Vec
import turtle
import font_loader

l1 = [(0, 1), (1, 2), (1, 0)]
l2 = [(0, 2), (1, 2), (1, 1), (0, 0), (1, 0)]
l3 = [(0, 2), (1, 2), (0, 1), (1, 1), (0, 0)]
l4 = [(0, 2), (0, 1), (1, 1), (1, 2), (1, 0)]
l5 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)]
l6 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, 1), (1, 2)]
l7 = [(0, 0), (0, 1), (1, 2), (0, 2)]
l8 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, 2), (1, 2), (1, 0)]
l9 = [(0, 0), (1, 1), (1, 2), (0, 2), (0, 1), (1, 1)]
l0 = [(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)]
symbols = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]

symbols = font_loader.load("arial.txt")


def print_number(turtle, number: int):
    start_point = turtle.pos()
    coords = symbols[number]
    turtle.penup()
    turtle.goto(start_point + font_size * Vec(*coords[0]))
    turtle.pendown()
    for coord in coords:
        turtle.goto(start_point + font_size * Vec(*coord))
    turtle.penup()
    turtle.goto(start_point + font_size * Vec(1, 0))


def print_numbers(turtle, numbers):
    for number in numbers:
        print_number(turtle, number)
        turtle.goto(turtle.pos() + Vec(margin, 0))


if __name__ == "__main__":
    turtle.penup()
    turtle.goto(-200, 0)
    print_numbers(turtle, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    turtle.done()
