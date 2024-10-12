import turtle

sc = turtle.Screen()
turtle = turtle.Turtle()
size = 30
def draw_square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_grid():
    start_y = 300  
    for row in range(20):
        for col in range(20):
            x = col * size - 300  
            y = start_y - row * size  
            color = 'black' if (row + col) % 2 == 0 else 'red'
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            draw_square(color)


turtle.speed(0)  
turtle.color('black')

draw_grid()