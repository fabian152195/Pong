import tkinter.messagebox
from tkinter import *
import time
HEIGHT=500
WIDTH = 800
pantalla = Tk()
pantalla.minsize(WIDTH, HEIGHT)
pantalla.title("PONG")

c = Canvas(pantalla, width=WIDTH, height = HEIGHT, bg = "black")
c.pack()


p1 = [0, 20]
p2 = [780, 800]

class Jugador:
    velocidad = 1
    color_paleta = "black"
    def __init__(self, size,player):
        self.shape = c.create_rectangle(player[0], 0,player[1] , size, fill="white")


        """self.color_paleta = ""
        self.velocidad = velocidad
        self.posiciony =
        self.posicionx ="""

class Juego:

    modo = ''
    paletas = 1
    puntaje = []
    nivel = 1

    def __init__(self, modo, paletas, puntaje, nivel):
        self.matriz = [ [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False] ]
        self.Puntaje = puntaje
        self.modo = modo
        self.paletas = paletas
        self.nivel = nivel
    def set_nivel(self):
        self.nivel = 1 #entrada del programa  ## para mofi
        return self.nivel

    def cambiar_nivel(self):
        if ((self.puntaje[0] == 7 or self.puntaje[1] == 7) and self.nivel<=3):
            self.nivel += 1

pad1 = Jugador(180, p1)
pad2 = Jugador(180,p2)

pantalla.mainloop()