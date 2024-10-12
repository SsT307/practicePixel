#Fatma Alsuwaidi Part
import turtle

def get_color(char):
    color_row = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    return color_row.get(char, None)

def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(10)
        turta.right(90)
    turta.end_fill()

def draw_pixel(color_string, turta):
    color = get_color(color_string)
    if color is None:
        return
    draw_color_pixel(color, turta)

def draw_line_from_string(color_string, turta):
    for char in color_string:
        color = get_color(char)
        if color is None:
            return False
        draw_pixel(char, turta)
        turta.penup()
        turta.forward(10)
        turta.pendown()
    return True

def draw_shape_from_string(turta):
    while True:
        user_input = input("Enter a color string (or press Enter to quit): ")
        if user_input == "":
            break
        if not draw_line_from_string(user_input, turta):
            break
        turta.penup()
        turta.goto(turta.xcor() - len(user_input) * 10, turta.ycor() - 10)
        turta.pendown()

def main():
    turta = turtle.Turtle()
    turta.speed(0)
    turtle.bgcolor('white')
    draw_shape_from_string(turta)
    turtle.done()

main()