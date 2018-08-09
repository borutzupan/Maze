import turtle

okno = turtle.Screen()
okno.bgcolor("black")
okno.title("Labirint")
okno.setup(700, 700)

class Pisalo(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("sqare")
        self.color("white")
        self.dvigni_pisalo
        self.speed(0)


