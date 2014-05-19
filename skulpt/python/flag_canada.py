#default
import turtle
tortue = turtle.Turtle()
tortue.speed(0)
tortue.ht()
tortue.setpos( 250 , 250 )
tortue.fillcolor('#123456')
tortue.begin_fill()

for _ in range(4):
    tortue.right(90)
    tortue.forward(500)
tortue.end_fill()



#tortue.ht()
#tortue.pu()

tortue.setpos( -40 , -40 )
tortue.fillcolor('red')
tortue.begin_fill()

for _ in range(2):
    tortue.left(90)
    tortue.forward(80)
    tortue.left(90)
    tortue.forward(40)
tortue.end_fill()

tortue.forward(80)


tortue.begin_fill()
tortue.fillcolor('white')
for _ in range(4):
    tortue.left(90)
    tortue.forward(80)
tortue.end_fill()    
# A VOUS DE TERMINER LE DRAPEAU FRANCAIS
# EN RAJOUTANT LES ORDRES NECESSAIRES
# TENTEZ DE DESSINER D'AUTRES DRAPEAUX
#
tortue.forward(40)
tortue.fillcolor('red')
tortue.begin_fill()
for _ in range(2):
    tortue.left(90)
    tortue.forward(80)
    tortue.left(90)
    tortue.forward(40)
tortue.end_fill() 
#tortue.setpos(0,-30)
#tortue.backward(30)
#for _ in range(4):
#  tortue.forward(60)
#  tortue.left(90)
tortue.begin_fill()
tortue.setpos(0,-30)
tortue.left(90)
tortue.goto(0,12-30)
tortue.goto(-15,10-30)
tortue.goto(-13,15-30)
tortue.goto(-30,28-30)
tortue.goto(-26,30-30)
tortue.goto(-29,40-30)
tortue.goto(-20,38-30)
tortue.goto(-18,43-30)
tortue.goto(-10,35-30)
tortue.goto(-12,52-30)
tortue.goto(-7,50-30)
tortue.goto(0,60-30)
tortue.goto(7,50-30)
tortue.goto(12,52-30)
tortue.goto(10,35-30)
tortue.goto(18,43-30)
tortue.goto(20,38-30)
tortue.goto(29,40-30)
tortue.goto(26,30-30)
tortue.goto(30,28-30)
tortue.goto(13,15-30)
tortue.goto(15,10-30)
tortue.goto(0,12-30)
tortue.end_fill()
