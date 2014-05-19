__author__ = 'mistert'

"""
Ce programme est l'oeuvre exclusive de MisterT <sebastien.tack@sfr.fr>
"""

import turtle
def doc():
    return "geom1 = mistert.Geometrie(x, y , angle, couleur1, couleur2, visible )"

class Geometrie(turtle.Turtle):
    def __init__(self, x = 0, y = 0, angle = 0 , couleur1 = 'black', couleur2 = 'white', visible = True):
        self.__tortue = turtle.Turtle()
        self.__tortue.setpos(x, y)
        self.__x = x
        self.__y = y
        self.__angle = angle
        self.__couleur1 = couleur1
        self.__couleur2 = couleur2
        self.__tortue.color(self.__couleur1)
        self.__tortue.fillcolor(self.__couleur2)
        self.__tortue.left(angle)
        if not(visible):
            self.__tortue.ht()

    def donne_tortue(self):
        return self.__tortue
    def mettre_angle(self,val):
        self.__angle = val
    def donne_angle(self):
        return self.__angle
    def mettre_x(self,val):
        self.__x = val
    def donne_x(self):
        return self.__x
    def mettre_y(self,val):
        self.__y = val
    def donne_y(self):
        return self.__y
    def mettre_couleur1(self,val):
        self.__couleur1 = val
        self.__tortue.color(self.__couleur1)

    def donne_couleur1(self):
        return self.__couleur1
    def mettre_couleur2(self,val):
        self.__couleur2 = val
        self.__tortue.fillcolor(self.__couleur2)

    def donne_couleur2(self):
        return self.__couleur2

    def positionne(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        self.__tortue.setpos( x , y )


    def carre(self,longueur = 50, plein = False):
        self.__tortue.setpos(self.__x, self.__y)
        if plein:
              self.__tortue.begin_fill()
        for i in range(4):
            self.__tortue.forward(longueur)
            self.__tortue.left(90)
        if plein:
              self.__tortue.end_fill()

    def polygone(self,longueur = 50, n = 6, plein = False):
        self.__tortue.setpos(self.__x, self.__y)
        if plein:
              self.__tortue.begin_fill()
        for i in range(n):
            self.__tortue.forward(longueur)
            self.__tortue.left(360 // n)
        if plein:
              self.__tortue.end_fill()


    def rectangle(self,longueur = 50, largeur = 50, plein = False):
        self.__tortue.setpos(self.__x, self.__y)
        if plein:
              self.__tortue.begin_fill()
        for i in range(4):
            self.__tortue.forward(longueur)
            self.__tortue.left(90)
            self.__tortue.forward(largeur)
            self.__tortue.left(90)
        if plein:
              self.__tortue.end_fill()


    def cercle(self,rayon, plein = False):
         self.__tortue.setpos(self.__x, self.__y)
         if plein:
              self.__tortue.begin_fill()
         self.__tortue.circle(rayon)
         if plein:
              self.__tortue.end_fill()

    def cacher(self):
         self.__tortue.ht()
         

if __name__ == '__main__':
    geom1 = Geometrie(0, 0 , 0, 'Black', 'Black', True )
