#Link do python dokumentacije za class turtle: https://docs.python.org/3.0/library/turtle.html
import turtle
import math


#Ozadje
okno = turtle.Screen()
okno.bgcolor("black")
okno.title("Lovci na zaklade")
okno.setup(1200, 700)
okno.tracer(7)

#Slike
slike = ["treasure.gif", "wall.gif", "dwarf.gif", "flame.gif", "orc.gif", "lava.gif"]
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


class Lovec_na_zaklade(turtle.Turtle):
    def __init__(self, ime, oblika):
        turtle.Turtle.__init__(self)
        self.shape(oblika)
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.ime = ime

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

    def smrt(self):
        self.gold -= 50
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-520, 250)
        turtle.color("red")
        turtle.write("""{}, umru si!
Št. kovancev -50""".format(self.ime), False, font=("Arial", 16, "normal"))
        turtle.ontimer(turtle.undo(), 1000)

    def našel_zaklad(self):
        self.gold += zaklad.gold
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-550, 150)
        turtle.color("gold")
        turtle.write("""Število zlatih
kovancev ({}): {}""".format(self.ime, self.gold), False, font=("Arial", 14, "normal"))
        turtle.ontimer(turtle.undo(), 1000)
        zaklad.zaklad_pobran()
        zakladi.remove(zaklad)

    
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

class Lava(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("lava.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        
#Nivoji
nivo = [""]

nivo_1 = [
    "XXXXXLLLLLLLLXXXXXXXXXXXX",
    "X12XXXLLLLLL        XXXXX",
    "X  XXXXLLLL  XXXXXO XXXXX",
    "X     OLLX  XXXXXX  XXXXX",
    "X      OLX  XXX    O  TXX",
    "XXXXXX OXX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "XT XXX      O XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X  OO    OXXXXXXXXXXXXXXX",
    "X     O          XXXXXXXX",
    "XXXXXXXXXXXXOOO  XXXXXTOX",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX TXXXXXXXXXX  O    O X",
    "XXX O   O           O   X",
    "XXX   O     XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX      O      TX",
    "XX T XXXXX   O          X",
    "LX  OXXXXXXXXXXXXX  XXXXX",
    "LL  OOXXXXXXXXXXXX  XXXXX",
    "LLL  OO     XXXX O      X",
    "LLLL                 O TX",
    "LLLLLXXXXXXXXXXXXXXXXXXXX"
    ]

zakladi = []
ovire = []
začetki = []

nivo.append(nivo_1)

#Uporabne funkcije
def nariši_labirint(NIVO):
    for y in range(len(NIVO)):
        for x in range(len(NIVO[y])):
          znak = NIVO[y][x]
          x_platno = -288 + (x * 24)
          y_platno = 288 - (y * 24)

          if znak == "L":
              ovire.append(Lava(x_platno, y_platno))

          if znak == "O":
              ovire.append(Ogenj(x_platno, y_platno))
              
          if znak == "T":
              zakladi.append(Zaklad(x_platno, y_platno))

          if znak == "1":
              Lovec_1.goto(x_platno, y_platno)
              začetki.append((x_platno, y_platno))

          if znak == "2":
              Lovec_2.goto(x_platno, y_platno)
              začetki.append((x_platno, y_platno))

          if znak == "X":
              pisalo.goto(x_platno, y_platno)
              pisalo.shape("wall.gif")
              pisalo.stamp()
              zid.append((x_platno, y_platno))



#Osebe
pisalo = Pisalo()
Lovec_1 = Lovec_na_zaklade("Lovec 1", "dwarf.gif")
Lovec_2 = Lovec_na_zaklade("Lovec 2", "orc.gif")

zid = []

nariši_labirint(nivo[1])

#Tipke
turtle.listen()
turtle.onkey(Lovec_1.gor, "w")
turtle.onkey(Lovec_1.dol, "s")
turtle.onkey(Lovec_1.levo, "a")
turtle.onkey(Lovec_1.desno, "d")
turtle.onkey(Lovec_2.gor, "Up")
turtle.onkey(Lovec_2.dol, "Down")
turtle.onkey(Lovec_2.levo, "Left")
turtle.onkey(Lovec_2.desno, "Right")




#mainloop()
while True:
    for zaklad in zakladi:
        if Lovec_1.zadetek(zaklad):
            Lovec_1.našel_zaklad()

    for zaklad in zakladi:
        if Lovec_2.zadetek(zaklad):
            Lovec_2.našel_zaklad()

    for ovira in ovire:
        if Lovec_1.zadetek(ovira):
            Lovec_1.smrt()
            Lovec_1.goto(začetki[0])

    for ovira in ovire:
        if Lovec_2.zadetek(ovira):
            Lovec_2.smrt()
            Lovec_2.goto(začetki[1])


    okno.update()
    if zakladi == []:
        turtle.bye()
        print("Lovec 1: {}".format(Lovec_1.gold))
        print("Lovec 2: {}".format(Lovec_2.gold))
        if Lovec_1.gold > Lovec_2.gold:
            print("Lovec 1 JE ZMAGAL!")
        elif Lovec_2.gold > Lovec_1.gold:
            print("Lovec 2 JE ZMAGAL!")
        elif Lovec_1.gold == Lovec_2.gold:
            print("IZENAČEN IZID!")

    





    
