import turtle
import time
import random

posponer = 0.1

score = 0
high_score = 0

#Window
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


#Red
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) 



#function
def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def izquierda():
    head.direction = "left"
def derecha():
    head.direction = "right"

#segment
segments = []

text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0         High Score: 0", align = "center", font=("Courier",24,"normal"))




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

#keyboard
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True: 
    wn.update()
    
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280  or head.ycor() <-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"

        for segment in segments:
            segment.goto(1000,1000)
        
        segments.clear()

        #
        score = 0
        text.clear()
        text.write("Score: {}      High Score: {}".format(score, high_score),
              align = "center", font=("Courier",24,"normal"))
             



#por defecto el cuadrado blanco es de 20 por 20 pixeles.
    if head.distance(food) < 20:
       x = random.randint(-280, 280)
       y = random.randint(-280, 280)
       food.goto(x,y)
       new_segment = turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("grey")
       new_segment.penup()
       segments.append(new_segment)

       #
       score += 1
       if score > high_score:
           high_score = score

       text.clear()
       text.write("Score: {}   High Score: {}".format(score, high_score),
              align = "center", font=("Courier",24,"normal"))
           
       

    totalSeg = len(segments)
    for index in range(totalSeg -1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if totalSeg > 0:
         x = head.xcor()
         y = head.ycor()
         segments[0].goto(x, y)

     

    mov()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments: 
                segment.goto(1000,1000)
            segments.clear()


            #
            score = 0 
            text.clear()
            text.write("Score: {}   High Score: {}".format(score, high_score),
              align = "center", font=("Courier",24,"normal"))

    time.sleep(posponer)