#Link do python dokumentacije za class turtle: https://docs.python.org/3.0/library/turtle.html
import turtle
import math

#Ozadje
okno = turtle.Screen()
okno.bgcolor("black")
okno.title("Lovec na relikte")
okno.setup(700, 700)
okno.tracer(0)

#Slike
slike = ["treasure.gif", "wall.gif", "dwarf.gif", "flame.gif"]
for slika in slike:
    turtle.register_shape(slika)

#Objekti
class Pisalo(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Lovec_na_relikte(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("dwarf.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def gor(self):
        naslednje_koor_x = self.xcor()
        naslednje_koor_y = self.ycor() + 24

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor(), self.ycor() + 24)

    def dol(self):
        naslednje_koor_x = self.xcor()
        naslednje_koor_y = self.ycor() - 24

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor(), self.ycor() - 24)

    def levo(self):
        naslednje_koor_x = self.xcor() - 24
        naslednje_koor_y = self.ycor()

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor() - 24, self.ycor())

    def desno(self):
        naslednje_koor_x = self.xcor() + 24
        naslednje_koor_y = self.ycor()

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor() + 24, self.ycor())

    def zadetek(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        oddaljenost = math.sqrt((a ** 2) + (b ** 2))

        if oddaljenost < 5:
            return True
        else:
            False

            
class Zaklad(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def zaklad_pobran(self):
        self.hideturtle()


class Ogenj(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("flame.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        
#Nivoji
nivo = [""]

nivo_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X12XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXXO XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX    O   XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "XT XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

zakladi = []
ovire = []
začetki = []

nivo.append(nivo_1)

def nariši_labirint(NIVO):
    for y in range(len(NIVO)):
        for x in range(len(NIVO[y])):
          znak = NIVO[y][x]
          x_platno = -288 + (x * 24)
          y_platno = 288 - (y * 24)

          if znak == "O":
              ovire.append(Ogenj(x_platno, y_platno))
              
          if znak == "T":
              zakladi.append(Zaklad(x_platno, y_platno))

          if znak == "1":
              lovec1.goto(x_platno, y_platno)
              začetki.append((x_platno, y_platno))

          if znak == "2":
              lovec2.goto(x_platno, y_platno)
              začetki.append((x_platno, y_platno))

          if znak == "X":
              pisalo.goto(x_platno, y_platno)
              pisalo.shape("wall.gif")
              pisalo.stamp()
              zid.append((x_platno, y_platno))


#Osebe
pisalo = Pisalo()
lovec1 = Lovec_na_relikte()
lovec2 = Lovec_na_relikte()

zid = []

nariši_labirint(nivo[1])

#Tipke
turtle.listen()
turtle.onkey(lovec1.gor, "w")
turtle.onkey(lovec1.dol, "s")
turtle.onkey(lovec1.levo, "a")
turtle.onkey(lovec1.desno, "d")
turtle.onkey(lovec2.gor, "Up")
turtle.onkey(lovec2.dol, "Down")
turtle.onkey(lovec2.levo, "Left")
turtle.onkey(lovec2.desno, "Right")


#mainloop()
while True:
    for zaklad in zakladi:
        if lovec1.zadetek(zaklad):
            lovec1.gold += zaklad.gold
            print("Število zlatih kovancev (Lovec 1): {}".format(lovec1.gold))
            zaklad.zaklad_pobran()
            zakladi.remove(zaklad)
        elif lovec2.zadetek(zaklad):
            lovec2.gold += zaklad.gold
            print("Število zlatih kovancev (Lovec 2): {}".format(lovec2.gold))
            zaklad.zaklad_pobran()
            zakladi.remove(zaklad)

    for ogenj in ovire:
        if lovec1.zadetek(ogenj):
            print("Lovec 1, umru si!")
            lovec1.goto(začetki[0])
        elif lovec2.zadetek(ogenj):
            print("Lovec 2, umru si!")
            lovec2.goto(začetki[1])
            

    okno.update()





    
