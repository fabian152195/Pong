import tkinter.messagebox
from tkinter import *

pantalla = Tk()
pantalla.minsize(800, 500)
pantalla.title("PONG")
pantalla.configure(bg="black")


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

