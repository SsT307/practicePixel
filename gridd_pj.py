import turtle

sc = turtle.Screen()
turtle = turtle.Turtle()

def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_grid():
    size = 30
    start_y = 300  
    for row in range(20):
        for col in range(20):
            x = col * size - 300  
            y = start_y - row * size  
            color = 'black' if (row + col) % 2 == 0 else 'red'
            draw_square(x, y, size, color)

def draw_line_from_string(line_string):
    points = line_string.split(';')
    for point in points:
        x, y = map(int, point.split(','))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + 30, y + 30)  

turtle.speed(0)  
turtle.color('black')

draw_grid()