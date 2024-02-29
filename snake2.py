import turtle

wn = turtle.Screen()
wn.title("Game Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#wn.mainloop()


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0) 
head.direction ="stop"

#function
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety( y + 20)
    


while True: 
    wn.update()

