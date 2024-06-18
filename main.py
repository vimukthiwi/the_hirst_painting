# Import the necessary libraries
import random
import turtle

# Set the color mode to RGB
turtle.colormode(255)

# List of colors in RGB format
color_list = [
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5),
    (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161),
    (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206),
    (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
    (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239),
    (217, 88, 51)
]

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Set the pen size
t.width(5)

# Function to draw a painting using random colors from the color_list
def draw_paint():
    for _ in range(10):
        for _ in range(10):
            t.penup()
            t.color(random.choice(color_list))
            t.dot()
            t.forward(20)
        t.backward(200)
        t.right(90)
        t.forward(20)
        t.left(90)

# Call the draw_paint function to draw the painting
draw_paint()

# Keep the window open
screen.mainloop()
