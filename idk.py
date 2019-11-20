import turtle 

bob = turtle.Turtle()
turtle.bgcolor("black")
sides = 5
color = ["purple","blue","green","orange","red"]
for star in range(60):
    bob.forward(star * 20)
    bob.right(144)
    bob.pencolor(color[star%sides])
    
turtle.done()
