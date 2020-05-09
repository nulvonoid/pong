#bukan OOP
# https://www.youtube.com/watch?v=9LhS5IFh78I

import turtle 

layar = turtle.Screen()
layar.title('Pong')
layar.bgcolor("black")
layar.setup(width=800, height=800)
layar.tracer(0)

#raket A
raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape("square")
raket_a.color("white")
raket_a.shapesize(stretch_wid=5,stretch_len=1)
raket_a.penup()
raket_a.goto(-350,0)

#raket B
raket_b = turtle.Turtle()
raket_b.speed(0)
raket_b.shape("square")
raket_b.color("white")
raket_b.shapesize(stretch_wid=5,stretch_len=1)
raket_b.penup()
raket_b.goto(350,0)


#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)

#loop utama
while True:                                     #awalmya raket ga muncul, ternyata ini harus ditaro di bagian akhir 
   layar.update()