#bukan OOP
# https://www.youtube.com/watch?v=9LhS5IFh78I

import turtle 
import os 

layar = turtle.Screen()
layar.title('Pong')
layar.bgcolor("black")
layar.setup(width=800, height=600)
layar.tracer(0)

#skor
skor_a = 0
skor_b = 0


#raket A kiri
raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape("square")
raket_a.color("white")
raket_a.shapesize(stretch_wid=5,stretch_len=1)
raket_a.penup()
raket_a.goto(-350,0)

#raket B kanan
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
bola.dx = 0.2 
bola.dy = 0.2

# pen
skor = turtle.Turtle()
skor.speed(0)
skor.color ('white')
skor.penup()
skor.hideturtle()
skor.goto(0,260)
skor.write("Player A: 0  Player B:0", align="center",font=("Courier", 24, "normal"))



#function
def raket_a_atas():
    y = raket_a.ycor()
    y +=20
    raket_a.sety(y)

def raket_a_bawah():
    y = raket_a.ycor()
    y -=20
    raket_a.sety(y)

def raket_b_atas():
    y = raket_b.ycor()
    y +=20
    raket_b.sety(y)

def raket_b_bawah():
    y = raket_b.ycor()
    y -=20
    raket_b.sety(y)



#kibord
layar.listen()
layar.onkeypress(raket_a_atas, "w")                 #konsensus kalo huruf kecil, kalo arrow keys kapital awalnya
layar.onkeypress(raket_a_bawah, "s")
layar.onkeypress(raket_b_atas, "Up")
layar.onkeypress(raket_b_bawah, "Down")


#loop utama
while True:                                     #awalmya raket ga muncul, ternyata ini harus ditaro di bagian akhir 
    layar.update()

   #bola gerak
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

   #tumbukan sama border
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1            #ini bikin efek tumbukan. reverse direction.
        os.system("aplay bounce.wav&")

    if bola.xcor() > 390 :
        bola.goto(0,0)
        bola.dx *= -1
        skor_a += 1
        skor.clear()
        skor.write("Player A: {}  Player B: {}".format(skor_a,skor_b), align="center",font=("Courier", 24, "normal"))

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1            #ini bikin efek tumbukan. reverse direction.
        os.system("aplay bounce.wav&")

    if bola.xcor() < -390 :
        bola.goto(0,0)
        bola.dx *= -1
        skor_b += 1
        skor.clear()
        skor.write("Player A: {}  Player B: {}".format(skor_a,skor_b), align="center",font=("Courier", 24, "normal"))
        


    #tumbukan raket kanan 
    if (bola.xcor() > 340 and bola.xcor() <350 ) and (bola.ycor() < raket_b.ycor() + 40 and bola.ycor() > raket_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1
        os.system("aplay bounce.wav&")


    # tumbukan raket kiri
    if (bola.xcor() < -340 and bola.xcor() > -350 ) and (bola.ycor() < raket_a.ycor() + 40 and bola.ycor() > raket_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1
        os.system("aplay bounce.wav&")
#finish.