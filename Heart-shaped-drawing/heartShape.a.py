import turtle

def draw_heart():
    # Set the speed of the turtle
    turtle.speed(10)

    # Move the turtle to the starting position
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

    # Draw the heart shape
    turtle.begin_fill()
    turtle.color("red")
    turtle.left(140)
    turtle.forward(111.65)
    turtle.circle(-100, 50)
    turtle.right(50)
    turtle.circle(-100, 50)
    turtle.forward(111.65)
    turtle.end_fill()

    # Hide the turtle and exit the turtle window
    turtle.hideturtle()
    turtle.done()

# Call the draw_heart function
draw_heart()
