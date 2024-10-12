import turtle

turta = turtle.Turtle()
size = 30

# ------------------------------ color as number ----------------------------- #
# Function to get color based on character input
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
    
def draw_pixel(color, turta):
    turta.fillcolor(color)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(size)
        turta.right(90)
    turta.end_fill()
    
# ---------------------------- red and black grid ---------------------------- #
def draw_pixel(color, turta):
    turta.fillcolor(color)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(size)
        turta.right(90)
    turta.end_fill()
    
def draw_grid(turta):
    start_y = 300  
    for row in range(20):
        for col in range(20):
            x = col * size - 300  
            y = start_y - row * size  
            color = 'black' if (row + col) % 2 == 0 else 'red'
            turta.penup()
            turta.goto(x, y)
            turta.pendown()
            draw_pixel(color, turta)

# Function to draw a line from a string of color characters
def draw_line_from_string(color_string, turta):
    for char in color_string:
        if get_color(char) is None:  # Check for invalid color
            return False
        draw_pixel(char, turta)  # Draw pixel for each character
    return True
            
# ------------------------------ draw from file ------------------------------ #
# Function to draw shapes from a file (modified)
def draw_from_file(turta):
    # Prompt the user to enter the file name
    file_name = input("Enter the path of the file that you want to read its content: ")

    try:
        # Open the file and read its content
        with open(file_name, 'r') as file:
            print(f"Reading from {file_name}...")

            # Start drawing each line from the file
            for line in file:
                line = line.strip()  # Remove extra spaces or newlines
                if line:  # If the line is not empty
                    result = draw_line_from_string(line, turta)
                    if not result:  # If an invalid character is found, stop drawing
                        print(f"Invalid color in line: {line}")
                        break
                # Move the turtle to the next line (start of a new row)
                turta.penup()
                turta.backward(20 * len(line))  # Move back to the start of the row
                turta.right(90)
                turta.forward(size)  # Move down to the next row
                turta.left(90)
                turta.pendown()

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# ----------------------------- draw from string ----------------------------- #
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(10)
        turta.right(90)
    turta.end_fill()

def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(size)
        turta.right(90)
    turta.end_fill()
    draw_pixel(color_string)

def draw_pixel(color_string):
    color = get_color(color_string)
    if color is None:
        return
    draw_color_pixel(color, turta)

def draw_line_from_string(color_string, turta):
    for char in color_string:
        color = get_color(char)
        if color is None:
            return False
        draw_pixel(char)
        turta.penup()
        turta.forward(size)
        turta.pendown()
    turta.penup()
    turta.backward(size * len(color_string))  # Move back to the start of the row
    turta.right(90)
    turta.forward(size)  # Move down to the next row
    turta.left(90)
    turta.pendown()
    return True

def draw_shape_from_string():
    while True:
        user_input = input("Enter a color string (or press Enter to quit): ")
        if user_input == "":
            break
        if not draw_line_from_string(user_input, turta):
            break
        
# ---------------------------- now asking the user --------------------------- #
def main():
    pick = input("Which type of grid would you like 1-Red&Black 2-ColorFromString 3-DrawFromFile: ")
    if pick == '1':
        draw_grid(turta)
    elif pick == '2':
        draw_shape_from_string()
    elif pick == '3':
        draw_from_file(turta)
    else:
        print("Invalid choice. Please choose 1, 2 or 3")

# ------------------------------ main execution ------------------------------ #
if __name__ == "__main__":
    turta.speed(10)
    main()