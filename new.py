import turtle

turtle.speed(1000000)
size = 30

# Function to get color based on character input
def get_color(char):
    color_map = {
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
    return color_map.get(char, None)

def draw_pixel(color):
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
            draw_pixel(color)
            

draw_grid()

def draw_line_from_string(color_string):
    for char in color_string:
        color = get_color(char)
        if color is None:
            return False
        draw_pixel(char)
        turta.penup()
        turta.forward(10)
        turta.pendown()
    return True
        
def draw_line_from_file(color_string):
    for char in color_string:
        if get_color(char) is None:  # Check for invalid color
            return False
        draw_pixel(char)  # Draw pixel for each character
    return True

def draw_shape_from_string():
    while True:
        user_input = input("Enter a color string (or press Enter to quit): ")
        if user_input == "":
            break
        if not draw_line_from_string(user_input):
            break

# Main execution to test the function
if __name__ == "__main__":
    # Initialize the turtle object
    turta = turtle.Turtle()

    # Set turtle speed (optional)
    turta.speed(10)

    # Call the function to draw from file
    draw_shape_from_string()

    # Ensure the turtle graphics window stays open
    turtle.done()