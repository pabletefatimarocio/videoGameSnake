import turtle
import time

posponer = 0.1

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
def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def izquierda():
    head.direction = "left"
def derecha():
    head.direction = "right"


def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety( y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety( y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx( x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx( x + 20)

#Teclado
wn.listen()
wn.onkepress(arriba,"Up")
wn.onkepress(abajo,"Down")
wn.onkepress(izquierda,"Left")
wn.onkepress(derecha,"Right")

while True: 
    wn.update()

    mov()
    time.sleep(posponer)