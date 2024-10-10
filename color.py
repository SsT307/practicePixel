def get_color(num):
    # set array with colors, and have it set in an array
    with open("colors.txt", "r") as file:
        for word in file:
            color = word.split(", ")
        return color[num]
    
get_color(int(input("Enter number: ")))


# let the user pick the imagine