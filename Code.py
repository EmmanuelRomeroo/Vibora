"""Snake con comida que se mueve al azar."""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Comprueba si un punto está dentro del área de juego."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Intenta mover la comida un paso en una dirección aleatoria."""
    step = choice([
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10),
    ])

    next_food = food.copy()
    next_food.move(step)

    if inside(next_food) and next_food not in snake:
        food.x = next_food.x
        food.y = next_food.y


def move():
    """Mueve la serpiente y la comida."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))

        # Genera comida en una posición libre.
        while True:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10

            if food not in snake:
                break
    else:
        snake.pop(0)
        move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
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