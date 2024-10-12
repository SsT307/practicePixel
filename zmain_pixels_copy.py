import turtle as t
pixel = 35

def get_color(num):
    # set array with colors, and have it set in an array
    with open("colors.txt", "r") as file:
        for word in file:
            color = word.split(", ")
        return color[num]
        
        
def draw_colored_pixel():
    pixel_num = int(input("Can you enter a number: "))
    color = get_color(pixel_num)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(35)
        t.left(90)
    t.setheading(0)
    t.end_fill()
    
            
        
        
draw_colored_pixel()
    
t.Screen().exitonclick()

