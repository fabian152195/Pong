from tkinter import *
import time
import random
from threading import Thread
import threading

HEIGHT=500
WIDTH = 800
pantalla = Tk()
pantalla.minsize(WIDTH, HEIGHT)
pantalla.title("PONG")

c = Canvas(pantalla, width=WIDTH, height=HEIGHT, bg="black")
c.pack()
#pantalla.update()

c.create_line(400, 0, 400, 500, fill='white')
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
izquierda = ["w",'s']
derecha = ["<Up>", "<Down>"]

class paleta:
    color_paleta = 'white'
    posicion = []
    width = [0,0]
    height = [0,0]
    shape = None

    def __init__(self, canvas, height, width, lado):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(width[0], height[0], width[1], height[1], fill='white')
        self.posicion = canvas.coords(self.shape)
        self.y = 0
        self.canvas.bind_all(lado[0], self.up)
        self.canvas.bind_all(lado[1], self.down)

    def up(self, event):
        self.y = -20
    def down(self, event):
        self.y = 20
    def mover(self):
        self.canvas.move(self.shape, 0, self.y)
        self.set_posicion(0,self.y,0,self.y)
        Juego.modificar_matriz(Juego, self.get_posicion())
#        Juego.hace_Cero(Juego, self.get_posicion())
        pos = self.posicion
        if pos[1] < 0:
            self.y = 0
        if pos[3] > 500:
            self.y = 0
    def set_tamano(self,height):
        self.shape = c.create_rectangle(0, height[0], 20, height[1], fill='white')

    def set_color(self,color):
        self.shape = c.create_rectangle(self.width[0], self.height[0], self.width[1], self.height[1], fill=str(color))

    def get_posicion(self):
        return self.posicion
    def set_posicion(self, x1,y1,x2,y2):
        self.posicion[0]+=x1
        self.posicion[1]+=y1
        self.posicion[2]+=x2
        self.posicion[3]+=y2
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



class Bolita:

    def __init__(self):

        self.shape = c.create_oval(385, 235, 415, 265, fill = "red")
        self.xspeed = -20
        self.yspeed = 20
        self.pos = c.coords(self)

    def get_pos(self):
        return c.coords(self.shape)

    def move(self):
        c.move(self.shape, self.xspeed, self.yspeed)

        if self.get_pos()[3] >= HEIGHT or self.get_pos()[1] <= 0:
            self.yspeed = -self.yspeed
        if self.get_pos()[2] >= WIDTH or self.get_pos()[0] <= 0:
            self.xspeed = -self.xspeed




class Juego:
    paletas = 1
    modo = 'single'
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
        for i in range(int(pos[1])//20, int(pos[3])//20-1):
            for j in range(int(pos[0])//20, int(pos[2])//20):
                self.matriz[i][j] = 1
    def hace_Cero(self, pos):
        for i in range(26):
            for j in range(41):
                if i not in range(int(pos[1]) // 20, int(pos[3]) // 20 - 1) and j not in range(int(pos[0]) // 20,
                                                                                               int(pos[2]) // 20):
                    self.matriz[i][j] = 0


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
#JuegoPrincipal = Juego()

pad1 = paleta(c, grande, p1, lado=izquierda)
pad2 = paleta(c, grande, p2, lado=derecha)
Juego.modificar_matriz(Juego, pad1.get_posicion())
Juego.modificar_matriz(Juego, pad2.get_posicion())


bola = Bolita()

prnt_m(Juego.matriz)

while True:
    pad1.mover()
    pad2.mover()
    bola.move()
    prnt_m(Juego.matriz)
    pantalla.update()
    time.sleep(0.05)


pantalla.mainloop()

