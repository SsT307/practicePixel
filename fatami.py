# Import the turtle module
import turtle


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


# Function to draw a colored pixel
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):  # Draw a square pixel
        turta.forward(20)  # Adjust size as needed
        turta.right(90)
    turta.end_fill()
    turta.forward(20)  # Move to the right for the next pixel


# Function to draw a pixel using color string
def draw_pixel(color_string, turta):
    color = get_color(color_string)
    if color:
        draw_color_pixel(color, turta)


# Function to draw a line from a string of color characters
def draw_line_from_string(color_string, turta):
    for char in color_string:
        if get_color(char) is None:  # Check for invalid color
            return False
        draw_pixel(char, turta)  # Draw pixel for each character
    return True


# Function to draw shapes from a file (modified)
def draw_shape_from_string(turta):
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
                turta.forward(20)  # Move down to the next row
                turta.left(90)
                turta.pendown()

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main execution to test the function
if __name__ == "__main__":
    # Initialize the turtle object
    turta = turtle.Turtle()

    # Set turtle speed (optional)
    turta.speed(0)

    # Position turtle at the starting point (optional)
    turta.penup()
    turta.goto(-200, 200)  # Move to top-left of the screen
    turta.pendown()

    # Call the function to draw from file
    draw_shape_from_string(turta)

    # Ensure the turtle graphics window stays open
    turtle.done()