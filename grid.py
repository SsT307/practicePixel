import turtle as t
from main_pixels import draw_colored_pixel

rows = int(input("How many rows would you like to have: "))
columns = int(input("How many columns would you like to have: "))

def draw_grid():
    t.goto(-columns/2, -rows/2)
    count = 0
    while True:
        count += 1
        draw_colored_pixel()
        if count > rows:
            break
            
        
        
draw_grid()
