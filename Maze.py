#Link do python dokumentacije za class turtle: https://docs.python.org/3.0/library/turtle.html
import turtle

okno = turtle.Screen()
okno.bgcolor("black")
okno.title("Labirint")
okno.setup(700, 700)

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
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def gor(self):
        naslednje_koor_x = lovec.xcor()
        naslednje_koor_y = lovec.ycor() + 24

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor(), self.ycor() + 24)

    def dol(self):
        naslednje_koor_x = lovec.xcor()
        naslednje_koor_y = lovec.ycor() - 24

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor(), self.ycor() - 24)

    def levo(self):
        naslednje_koor_x = lovec.xcor() - 24
        naslednje_koor_y = lovec.ycor()

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor() - 24, self.ycor())

    def desno(self):
        naslednje_koor_x = lovec.xcor() + 24
        naslednje_koor_y = lovec.ycor()

        if (naslednje_koor_x, naslednje_koor_y) not in zid:
            self.goto(self.xcor() + 24, self.ycor())

nivo = [""]

nivo_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XZ XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
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

nivo.append(nivo_1)

def nariši_labirint(NIVO):
    for y in range(len(NIVO)):
        for x in range(len(NIVO[y])):
          znak = NIVO[y][x]
          x_platno = -288 + (x * 24)
          y_platno = 288 - (y * 24)

          if znak == "Z":
              lovec.goto(x_platno, y_platno)

          if znak == "X":
              pisalo.goto(x_platno, y_platno)
              pisalo.stamp()
              zid.append((x_platno, y_platno))


pisalo = Pisalo()
lovec = Lovec_na_relikte()

zid = []

nariši_labirint(nivo[1])

#tipke
turtle.listen()
turtle.onkey(lovec.gor, "w")
turtle.onkey(lovec.dol, "s")
turtle.onkey(lovec.levo, "a")
turtle.onkey(lovec.desno, "d")
turtle.onkey(lovec.gor, "Up")
turtle.onkey(lovec.dol, "Down")
turtle.onkey(lovec.levo, "Left")
turtle.onkey(lovec.desno, "Right")


#mainloop()
while True:
    okno.update()





    
