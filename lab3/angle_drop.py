import turtle
Vec = turtle.Vec2D


land_level = 0
time_k = 0.1
aerodinamic_k = 0.001
m = 0.1

def draw_land():
    turtle.goto(-500,land_level)
    turtle.goto(500, land_level)



if __name__ == "__main__":
    draw_land()
    turtle.goto(-200, 0)
    speed = Vec(25, 75)
    g = Vec(0, -1)
    while True:
        turtle.goto(turtle.pos() + speed * time_k)
        speed += g
        if abs(speed) > 5:
            f_aero = (-aerodinamic_k*speed) * abs(speed)
            speed += f_aero * m
        if turtle.pos()[1] < land_level:
            speed = Vec(speed[0], - speed[1])