import tkinter.messagebox
from tkinter import *
import time
import random

HEIGHT=500
WIDTH = 800
pantalla = Tk()
pantalla.minsize(WIDTH, HEIGHT)
pantalla.title("PONG")

c = Canvas(pantalla, width=WIDTH, height = HEIGHT, bg = "black")
c.pack()


p1 = [0, 20]
p2 = [780, 800]
grande = [160, 340]
mediano = [190, 310]
pequeno = [220,280]

# Clase paleta:
# Atributos:
#  color_paleta: string
#  posicion: list
#  width: int
#  height: int
#  shape: int
#######################
# Metodos:
#  __init__()
#  set_tamano()
#  set_color()
#  get_posicion()


class paleta:
    color_paleta = 'white'
    posicion = []
    width = [0,0]
    height = [0,0]
    shape = None

    def __init__(self, height, width):
        self.shape = c.create_rectangle(width[0], height[0], width[1], height[1], fill='white')
        self.posicion = c.coords(self.shape)

    def set_tamano(self,height):
        self.shape = c.create_rectangle(0, height[0], 20, height[1], fill='white')

    def set_color(self,color):
        self.shape = c.create_rectangle(self.width[0], self.height[0], self.width[1], self.height[1], fill=str(color))

    def get_posicion(self):
        return self.posicion

class Jugador(paleta):

    puntaje = 0 #puntaje por jugador
    paleta1= None
    paleta2= None
    shape = None

    def set_puntaje(self,puntaje):
        self.puntaje=puntaje

    def get_puntaje(self):
        return self.puntaje

    def mover_paletasUp(self,paleta1:paleta,paleta2:paleta=None):
        if paleta2==None:
            c.move(paleta1.shape, 0, -20)
            paleta1.get_posicion()

    def mover_paletasDown(self,paleta1:paleta,paleta2:paleta=None):
        if paleta2==None:
            c.move(paleta1.shape, 0, 20)
            paleta1.get_posicion()


class Bolita:

    def __init__(self):

        self.shape = c.create_oval(385, 235, 415, 265, fill = "red")
        self.xspeed = 5
        self.yspeed = 5
        pos = c.coords(self)

    def get_pos(self):
        return c.coords(self.shape)

    def move(self):
        c.move(self.shape, self.xspeed, self.yspeed)

        if self.get_pos()[3] >= HEIGHT or self.get_pos()[1] <= 0:
            self.yspeed = -self.yspeed
        if self.get_pos()[2] >= WIDTH or self.get_pos()[0] <= 0:
            self.xspeed = -self.xspeed




class Juego:
    #paletas = 1
    modo = ''
    puntaje = (0,0)
    nivel = 1
    jugador_izq = None
    jugador_der = None
    Bola = None
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, modo, paletas, puntaje, nivel, matriz):
        self.matriz = matriz
        self.Puntaje = puntaje
        self.modo = modo
        self.paletas = paletas
        self.nivel = nivel

    def set_nivel(self):
        self.nivel = 1 #entrada del programa  ## para modificar
        return self.nivel

    def cambiar_nivel(self):
        if ((self.puntaje[0] == 7 or self.puntaje[1] == 7) and self.nivel<=3):
            self.nivel += 1

    def modificar_matriz(self, pos):
        for i in range(int(pos[1])//20, int(pos[3])//20):
            for j in range(int(pos[0])//20, int(pos[2])//20):
                self.matriz[i][j] = 1

def prnt_m(matriz):
    for elemento in matriz:
        print(elemento)
def mv_dn(Juego, clase, objeto):
    clase.mover_paletasDown(clase, objeto)
    Juego.modificar_matriz(Juego, objeto.get_posicion())
    prnt_m(Juego.matriz)
def mv_up(Juego, clase, objeto):
    clase.mover_paletasUp(clase, objeto)
    Juego.modificar_matriz(Juego, objeto.get_posicion())
    prnt_m(Juego.matriz)

pantalla.bind("s", lambda event: mv_dn(Juego, Jugador, pad1))
pantalla.bind("S", lambda event: mv_dn(Juego, Jugador, pad1))
pantalla.bind("w", lambda event: mv_up(Juego, Jugador, pad1))
pantalla.bind("W", lambda event: mv_up(Juego, Jugador, pad1))

pantalla.bind("<Down>", lambda event: mv_dn(Juego, Jugador, pad2))
pantalla.bind("<Up>", lambda event: mv_up(Juego, Jugador, pad2))



pad1= paleta(pequeno,p1)
pad2 = paleta(pequeno,p2)

bola = Bolita()
Juego.modificar_matriz(Juego, pad1.get_posicion())
prnt_m(Juego.matriz)
while True:
    bola.move()
    pantalla.update()
    time.sleep(0.01)


pantalla.mainloop()

