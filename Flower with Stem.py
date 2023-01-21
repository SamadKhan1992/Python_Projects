import turtle

# flower
def bloom(tortoise, fcolor, length):
	tortoise.pencolor('red')
	tortoise.fillcolor(fcolor)
	tortoise.begin_fill()

	for segment in range(8):
		tortoise.forward(length)
		tortoise.left(135)

	tortoise.end_fill()

# Stem
def stem(tortoise, length):
	tortoise.pencolor('green')
	tortoise.pensize(length/20)
	tortoise.up()
	tortoise.forward(length/2)
	tortoise.down()
	tortoise.right(90)
	tortoise.forward(length)

# define a function to draw an entire flower
def flower(tortoise, fcolor, length):
	bloom(tortoise, fcolor, length)
	stem(tortoise, length)
	
# create a turtle object
george = turtle.Turtle()
george.hideturtle()
george.speed(7)

# draw flower
flower(george, 'yellow', 200)

screen=george.getscreen()
screen.exitonclick()