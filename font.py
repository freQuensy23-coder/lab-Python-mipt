from font_config import *

l1 = [(0,1), (1,2), (1,0)]
l2 = [(0,2), (1,2), (1,1), (0,0), (1, 0)]
l3 = [(0, 2), (1, 2), (0, 1), (1, 1), (0, 0)]
l4 = [(0, 2), (0, 1), (1, 1), (1, 2), (1, 0)]
l5 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1,2)]
l6 = [(0,0), (1, 0), (1,1), (0, 1), (0, 0), (0, 1), (1, 2)]
l7 = [(0,0), (0, 1), (1, 2), (0,2)]
l8 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, 2), (1, 2), (1, 0)]
l9 = [(0, 0), (1,1), (1,2), (0,2), (0,1),(1,1)]
l0 = [(0,0), (0,2), (1,2), (1, 0)]


symbols = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]
def print_number(turtle, number: int):
    start_point = turtle.pos()
    coords = symbols[number]
    turtle.pendown()
    for coord in coords:
        scale_goto(turtle, font_size, coord)
    turtle.pendown()
    turtle
def print_number_line(line: str, turtle):
    for letter in line:
        print_number(turtle, int(letter), )
        
    

def scale_goto(turtle, scale, coord):
    turtle.goto(coord[0] * scale, coord[1] * scale)

