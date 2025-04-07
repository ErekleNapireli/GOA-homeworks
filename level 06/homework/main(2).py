from turtle import *

speed(5)

width(2)

begin_fill()
color("gray")
#Right wing
forward(150)
left(55)
forward(250)
left(125)
forward(100)
left(55)
forward(125)

#Head part
right(145)
forward(100)
left(90)
forward(90)
left(90)
forward(100)

penup()
goto(0,0)
pendown()

#Left wing
right(145)
forward(250)
right(125)
forward(100)
right(55)
forward(125)

left(45)
forward(4)

end_fill()




exitonclick()