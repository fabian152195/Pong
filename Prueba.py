import tkinter.messagebox
import tkinter as tk
from tkinter import *
import time
import random
from threading import Thread
from tkinter import ttk
import threading

#VARIABLES POR UTILIZAR

HEIGHT = 500
WIDTH = 800
p1 = [0, 20]

p2 = [780, 800]
grande = [160, 340]
mediano = [190, 310]
pequeno = [220, 280]
bolaX= [400,420]
bolaY= [240,260]
izquierda = ["w", 's']
derecha = ["<Up>", "<Down>"]


#VARIABLES PARA CLASES

pantalla = Tk()
pantalla.minsize(WIDTH, HEIGHT)
pantalla.title("PONG")

c = Canvas(pantalla, width=WIDTH, height=HEIGHT, bg="black")
c.pack()

c.create_line(400, 0, 400, 500, fill='white')


#CLASES

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




class paleta: #clase que corresponde a las paletas
    color_paleta = 'white'
    posicion = []
    width = [0, 0]
    height = [0, 0]
    shape = None

    def __init__(self, canvas, height, width, lado):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(width[0], height[0], width[1], height[1], fill='white')
        self.posicion = canvas.coords(self.shape)
        print('este', self.posicion)
        self.y = 0
        print('este', lado[0], lado[1])
        self.canvas.bind_all(lado[0], self.up)
        self.canvas.bind_all(lado[1], self.down)
    #E: evento (presionar una tecla)
    #S: cambia el valor de la velocidad del pad, hacia arriba
    #R: -
    def up(self, event):  #permite mover el pad hacia arriba
        if int(self.get_posicion()[1]) > 0:
            self.y = -20

    # E: evento (presionar una tecla)
    # S: cambia el valor de la velocidad del pad, hacia abajo
    # R: -
    def down(self, event):
        if int(self.get_posicion()[3]) < HEIGHT:
            self.y = 20

    def mover(self):
        self.set_posicion(0, self.y, 0, self.y)
        self.canvas.move(self.shape, 0, self.y)
        Juego.modificar_matriz(Juego, self.get_posicion(), self.y)
        #prnt_m(Juego.matriz)
        pos = self.posicion
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = 0

    def set_tamano(self, height):
        self.shape = c.create_rectangle(0, height[0], 20, height[1], fill='white')

    def get_tamano(self):
        return self.height[1] - self.height[0]

    def set_color(self, color):
        self.shape = c.create_rectangle(self.width[0], self.height[0], self.width[1], self.height[1], fill=str(color))

    def get_posicion(self):
        return self.posicion

    def set_posicion(self, x1, y1, x2, y2):
        self.posicion[0] += x1
        self.posicion[1] += y1
        self.posicion[2] += x2
        self.posicion[3] += y2
        return self.posicion


class Jugador(paleta):
    puntaje = 0  # puntaje por jugador
    paleta1 = None
    paleta2 = None
    shape = None

    def set_puntaje(self, puntaje):
        self.puntaje = puntaje

    def get_puntaje(self):
        return self.puntaje


class Bolita:

    canvas = Canvas()

    def __init__(self,canvas,juegoClass):
        self.canvas = canvas
        self.juego = juegoClass
        self.shape = canvas.create_rectangle(400, 200, 420, 220, fill="white")
        self.xspeed = -20
        self.yspeed = 20
        self.pos = canvas.coords(self)
        print('posicion bola: ',self.pos)

    def get_pos(self):
        return self.canvas.coords(self.shape)

    def move(self):
        self.canvas.move(self.shape, self.xspeed, self.yspeed)
        print('pos bola: ',self.get_pos())
        if self.get_pos()[3] >= HEIGHT or self.get_pos()[1] <= 0:
            self.yspeed = -self.yspeed
        if self.get_pos()[0] // 20 == 1.0 and self.juego.matriz[int(self.get_pos()[3] // 20) - 1][
            int(self.get_pos()[0] // 20) - 1] \
                == 1 or \
                self.get_pos()[2] // 20 == 39.0 and self.juego.matriz[int(self.get_pos()[3] // 20) - 1][
            int(self.get_pos()[2]) // 20] \
                == 1:
            self.xspeed = -self.xspeed

        if int(self.get_pos()[0]) // 20 < 0:
            self.canvas.delete(self.shape)
            self.shape = self.canvas.create_rectangle(400, 200, 420, 220, fill="white")

            self.juego.set_puntaje2()
            print('entreeeeeeeeeeeeeeee: ', self.juego.puntaje2)
            self.juego.updatep2(self.juego.puntaje2)

            time.sleep(0.3)
        if int(self.get_pos()[2] // 20) > 40:
            self.canvas.delete(self.shape)
            self.shape=self.canvas.create_rectangle(400, 200, 420, 220, fill="white")
            self.juego.set_puntaje1()
            self.juego.updatep1(self.juego.puntaje1)
            time.sleep(0.3)
class Juego:
    paletas = 1
    modo = 'single'
    puntaje1 = 0
    puntaje2 = 0
    nivel = 1


    jugador_izq = None
    jugador_der = None
    Bola = None
    drawP1 = None
    drawP2 = None
    canvas = None
    matriz = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]]

    def __init__(self, canvas, modo=modo, paletas=paletas, nivel=nivel, matriz=matriz, puntaje1=puntaje1, puntaje2=puntaje2 ):
        self.matriz = matriz
        self.Puntaje1 = puntaje1
        self.Puntaje2 = puntaje2
        self.modo = modo
        self.paletas = paletas
        self.nivel = nivel
        self.drawP1 = canvas.create_text(175, 50,font=('', 40), text=str(0), fill='white')
        self.drawP2 = canvas.create_text(600, 50,font=('', 40), text=str(0), fill='white')
        self.canvas = canvas
        self.velocidad = 0.05


    def set_nivel(self):
        self.nivel = 1
        return self.nivel

    def cambiar_nivel(self):
        if ((self.puntaje[0] == 7 or self.puntaje[1] == 7) and self.nivel <= 3):
            self.nivel += 1

    def modificar_matriz(self, pos, cero):
        if cero == 20:
            self.matriz[(int(pos[1] // 20)) - 1][int(pos[0]) // 20] *= 0
        elif cero == -20:
            self.matriz[(int(pos[3]) // 20)][int(pos[0]) // 20] *= 0
        for i in range(int(pos[1]) // 20, int(pos[3]) // 20):
            for j in range(int(pos[0]) // 20, int(pos[2]) // 20):
                self.matriz[i][j] = 1
        return self.matriz

    def get_velocidad(self):
        return self.velocidad

    def set_puntaje1(self):
        self.puntaje1 += 1

    def set_puntaje2(self):
        self.puntaje2 += 1

    def updatep1(self, val):
        print('esto es: ', self.drawP1)
        self.canvas.delete(self.drawP1)

        self.drawP1 = self.canvas.create_text(170, 50,
                                             font=('', 40), text=str(val), fill='white')
    def updatep2(self, val):
        self.canvas.delete(self.drawP2)
        print('entre al update')

        self.drawP2 = self.canvas.create_text(600, 50, font=('', 40), text=str(val), fill='white')


def prnt_m(matriz):
    print('\n--------')
    for elemento in matriz:
        print(elemento)
def twopads(tamano):
    return paleta(c, tamano, p1, lado=izquierda), paleta(c, tamano, p2, lado=derecha)


#INSTANCIAS!!


#INSTANCIAS!!


pad2 = paleta(c, grande, p1, lado = izquierda)
pad4 = paleta(c, grande, p2, lado = derecha)



juegoPrincipal= Juego(c)

bola = Bolita(c, juegoPrincipal)

#CICLO


tiempo = 0.05

#CICLO
while True:
    print("izquierda" + str(Juego.puntaje1))
    print("derecha" + str(Juego.puntaje2))

    pad2.mover()
    pad4.mover()

    bola.move()
    print('matrizjuego')
    pantalla.update()
    time.sleep(Juego.get_velocidad(juegoPrincipal))