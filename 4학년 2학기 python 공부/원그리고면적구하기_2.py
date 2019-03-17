import turtle
pointx , pointy , radius = eval(input("Enter Point x , y , redius: "))

erea = radius * radius * 3.141592

turtle.penup()
turtle.goto(pointx , pointy-radius)
turtle.pendown()


turtle.circle(radius)

turtle.penup()
turtle.goto(pointx , pointy)
turtle.pendown()
turtle.write(int(erea*100)/100)
turtle.done()