import turtle
import math
import time
import random

#SENZAMI
zakladi = []
grmi = []
ovire = []
začetki = []
zid = []
mapa = []


#SLIKE
slike = [
    "female-zombie.gif", "male-zombie.gif", "human.gif", "treasure.gif",
    "wall.gif", "dwarf.gif", "flame.gif", "orc.gif", "lava.gif", "grm.gif",
    "archer.gif", "plant-golem.gif", "viking.gif", "vampire-viking.gif",
    "slime-red.gif"
    ]
imena_oseb = ["dwarf", "orc", "male-zombie", "female-zombie", "human",
              "viking", "vampire-viking", "plant-golem", "archer"]
def dodaj_slike(seznam):
    for slika in seznam:
        turtle.register_shape(slika)

dodaj_slike(slike)


#OBJEKTI
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
        self.zlato = 0
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
        self.zlato += -50
        print('')
        print("""{}, več sreče prihodnjič!
Št. kovancev -50""".format(self.ime))


    def našel_zaklad(self):
        self.zlato += zaklad.zlato
        print('')
        print("""Super {}!
Št. kovancev +100""".format(self.ime))
        zaklad.zaklad_pobran()
        zakladi.remove(zaklad)

    def našel_grm(self):
        self.zlato += grm.zlato
        print('')
        print("""Odlično {}!
Št. kovancev +{}""".format(self.ime, grm.zlato))
        grm.grm_preiskan()
        grmi.remove(grm)

    
class Zaklad(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.penup()
        self.speed(0)
        self.zlato = 100
        self.goto(x, y)

    def zaklad_pobran(self):
        self.hideturtle()


class Ogenj(turtle.Turtle):
    def __init__(self, x, y,):
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
        

class Grm(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("grm.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.zlato = random.randint(1, 100)

    def grm_preiskan(self):
        self.ht()


class Slime(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("slime-red.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        
 
#MAPE
def dodaj_mapo(ime_datoteke):
    with open(ime_datoteke) as vhodna:
        tabela = []
        for vrstica in vhodna:
            tabela.append(vrstica)
    return tabela

vrsta_mape = input("""Katero mapo bi radi?
mapa_1, mapa_2 ali mapa_3? """)

while True:
    if vrsta_mape in ['mapa_1', 'mapa_2', 'mapa_3']:
       mapa.append(dodaj_mapo(vrsta_mape + ".txt"))
       break
    else:
       print('')
       print("TE MAPE NI V SEZNAMU!")
       print('')
       vrsta_mape = input("""Katero mapo bi radi?
mapa_1, mapa_2 ali mapa_3? """)


#LABIRINT - FUNKCIJA
def nariši_labirint(MAPA):
    for y in range(len(MAPA)):
        for x in range(len(MAPA[y])):
          znak = MAPA[y][x]
          x_platno = -288 + (x * 24)
          y_platno = 288 - (y * 24)

          if znak == "R":
              ovire.append(Slime(x_platno, y_platno))

          if znak == "G":
              grmi.append(Grm(x_platno, y_platno))
            
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


#IZBIRA IMEN IN OSEBE
pisalo = Pisalo()
print('')
print("Igralec 1 uporablja tipke w, s, a, d")
print("Igralec 2 uporablja tipke Up, Down, Left, Right")
print('')
ime_1 = input("Igralec 1, vpiši svoje izbrano ime: ")
print('')
oseba_1 = input("""{}, izberi eneo iz med oseb
(dwarf, orc, male-zombie, female-zombie, human, viking, vampire-viking,
 plant-golem, archer)
ali pa se pusti presenetit (random): """.format(ime_1))

while True:
    if (oseba_1 != 'random') and (oseba_1 not in imena_oseb):
        print('')
        print("TE OSEBE NI V SEZNAMU!")
        print('')
        oseba_1 = input("""{}, izberi eneo iz med oseb
(dwarf, orc, male-zombie, female-zombie, human, viking, vampire-viking,
 plant-golem, archer)
ali pa se pusti presenetit (random): """.format(ime_1))
    else:
        break

print('')  
ime_2 = input("Igralec 2, vpiši svoje izbrano ime: ")
print('')
oseba_2 = input("""{}, izberi eneo iz med oseb
(dwarf, orc, male-zombie, female-zombie, human, viking, vampire-viking,
 plant-golem, archer)
ali pa se pusti presenetit (random): """.format(ime_2))

while True:
    if (oseba_2 != 'random') and (oseba_2 not in imena_oseb):
        print('')
        print("TE OSEBE NI V SEZNAMU!")
        print('')
        oseba_2 = input("""{}, izberi eneo iz med oseb
(dwarf, orc, male-zombie, female-zombie, human, viking, vampire-viking,
 plant-golem, archer)
ali pa se pusti presenetit (random): """.format(ime_2))
    else:
        break

if ime_1 != '' and oseba_1 != '':
    if oseba_1 == 'random':
        oseba_1 = random.choice(imena_oseb)
    Lovec_1 = Lovec_na_zaklade(ime_1, oseba_1 + ".gif")

if ime_2 != '' and oseba_2 != '':
    if oseba_2 == 'random':
        oseba_2 = random.choice(imena_oseb)
    Lovec_2 = Lovec_na_zaklade(ime_2, oseba_2 + ".gif")


#LABIRINT
if vrsta_mape != '':
    okno = turtle.Screen()
    okno.bgcolor("black")
    okno.title("Lovci na zaklade")
    okno.setup(700, 700)
    okno.tracer(8)

nariši_labirint(mapa[0])


#TIPKE
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

if vrsta_mape != '':
    while True:
        for zaklad in zakladi:
            if Lovec_1.zadetek(zaklad):
               Lovec_1.našel_zaklad()

        for zaklad in zakladi:
            if Lovec_2.zadetek(zaklad):
               Lovec_2.našel_zaklad()

        for grm in grmi:
            if Lovec_1.zadetek(grm):
               Lovec_1.našel_grm()

        for grm in grmi:
            if Lovec_2.zadetek(grm):
               Lovec_2.našel_grm()

        for ovira in ovire:
            if Lovec_1.zadetek(ovira):
               Lovec_1.goto(začetki[0])
               time.sleep(0.3)
               Lovec_1.smrt()
               
        for ovira in ovire:
            if Lovec_2.zadetek(ovira):
               Lovec_2.goto(začetki[1])
               time.sleep(0.3)
               Lovec_2.smrt()

               
        okno.update()
        if zakladi == []:
           turtle.penup()
           turtle.hideturtle()
           turtle.goto(25, 0)
           turtle.color("white")
           turtle.write("KONEC IGRE", False, align = "center", font=("Arial", 70, "bold"))
           time.sleep(2)
           turtle.bye()
           print('')
           print("{}: {}".format(Lovec_1.ime, Lovec_1.zlato))
           print("{}: {}".format(Lovec_2.ime, Lovec_2.zlato))
           print('')
           if Lovec_1.zlato > Lovec_2.zlato:
              print(Lovec_1.ime + " JE ZMAGAL!")
           elif Lovec_2.zlato > Lovec_1.zlato:
              print(Lovec_2.ime + " JE ZMAGAL!")
           elif Lovec_1.zlato == Lovec_2.zlato:
              print("IZENAČEN IZID!")

        


    





    
