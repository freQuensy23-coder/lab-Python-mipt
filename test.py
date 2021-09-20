
from math import atan
import turtle
from random import randint, random
 
 
number_of_turtles = number_of_turtle = 25
steps_of_the_time_number = 10000
 
 
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.turtlesize(0.4)
    unit.speed(250)
    unit.left(random() * 360)
    unit.goto(randint(-200, 200), randint(-200, 200))


 
for i in range(steps_of_the_time_number):
    for g in range(len(pool)):
        angle1 = pool[g].heading() 
        x1, y1 = pool[g].pos()     
        for h in range(len(pool)):  
            if g != h:
                x2, y2 = pool[h].pos()
                angle2 = pool[h].heading()
                dx = abs(x1-x2)    
                dy = max(abs(y1-y2), 0.1)    
                if dx <= 5 and dy <= 5:     # вместо корня можно считать по клеткам

                    teta = atan(dx/dy) * 57.2958
                    pool[g].seth(360 - angle1 + 2 * teta) # Посмотрите расчеты в этойформулы в документации
                    pool[h].seth(360 - angle2 + 2 * teta)
                    pool[h].fd(5.5)           
                    pool[g].fd(5.5)           

        # боковые стенки
        if x1 < -200 or x1 > 200:          
            pool[g].seth(180 - angle1)
        elif y1 < -200 or y1 > 200:         
            pool[g].seth(-angle1)
        pool[g].fd(7)
