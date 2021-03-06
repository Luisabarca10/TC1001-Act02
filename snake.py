"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['black', 'green', 'blue', 'yellow', 'brown']
random.shuffle(colors)
body_col = colors[0]
food_col = colors[1]
tick = 0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global tick
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)


        #mover comida
        tick += 1
        if tick >= 20:
            tick = 0
            # mover
            dirs = ['left', 'right', 'up', 'down']
            dir = random.choice(dirs)
            if dir == 'left':
                if food.x > -190:
                    food.x -= 10
            elif dir == 'right':
                if food.x < 200:
                    food.x += 10
            elif dir == 'up':
                if food.y < 200:
                    food.y += 10
            elif dir == 'down':
                if food.y > -190:
                    food.y -= 10 


    clear()

    for body in snake:
        square(body.x, body.y, 9, body_col)

    square(food.x, food.y, 9, food_col)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
