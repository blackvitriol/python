import turtle 

ninja = turtle.Turtle()

ninja.speed(10)

ninja.write("A7 was wondering.. why u watching this..", font=("Arial", 11, "normal"))

for i in range(180):
    ninja.forward(200)
    ninja.right(30)
    ninja.forward(30)
    ninja.left(70)
    ninja.forward(10)
    ninja.right(70)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()