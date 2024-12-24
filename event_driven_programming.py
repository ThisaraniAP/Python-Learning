import turtle

t = turtle.Turtle()
ts = t.getscreen()
t.shape("turtle")
t.color("green")
ts.bgcolor("black")

def forward():
    t.forward(3)

def left():
    t.left(90)

def right():
    t.right(90)

def spin():
    for i in range(4):
        t.right(90)

ts.onkey(forward, "space")
ts.onkey(left, "Left")
ts.onkey(right, "Right")
ts.onkey(spin, "s")

ts.listen()
