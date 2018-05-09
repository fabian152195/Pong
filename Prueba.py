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
#Player1_b=Button(pantalla, text = "abajo", command = lambda: Jugador.abajo(pad1))

#PLayer1_b2=Button(pantalla, text = "arriba", command = lambda: Jugador.arriba(pad1))

p1 = [0, 20]
p2 = [780, 800]
grande = [160, 340]
mediano = [190, 310]







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
    #velocidad = 1  INNECESARIO
    #color_paleta = "black"  EN LA CLASE PALETA
    '''
    def arriba(self):
        c.move(self.shape, 0, -20)
    def abajo(self):
        c.move(self.shape, 0, 20)
        '''
    def set_puntaje(self,puntaje):
        self.puntaje=puntaje

    def get_puntaje(self):
        return self.puntaje

    def mover_paletasUp(self,paleta1:paleta,paleta2:paleta=None):
        if paleta2==None:
            c.move(paleta1.shape, 0, -20)

    def mover_paletasDown(self,paleta1:paleta,paleta2:paleta=None):
        if paleta2==None:
            c.move(paleta1.shape, 0, 20)


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
    matriz = [[],[]]

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
        self.nivel = 1 #entrada del programa  ## para modificar
        return self.nivel

    def cambiar_nivel(self):
        if ((self.puntaje[0] == 7 or self.puntaje[1] == 7) and self.nivel<=3):
            self.nivel += 1


pad1= paleta(mediano,p1)
pad2 = paleta(mediano,p2)


pantalla.bind("s" , lambda event: Jugador.mover_paletasDown(Jugador,pad1))
pantalla.bind("w" , lambda event: Jugador.mover_paletasUp(Jugador,pad1))
#pantalla.bind("<Up>" , lambda event: Jugador.arriba(pad2))
#pantalla.bind("<Down>" , lambda event: Jugador.abajo(pad2))
bola = Bolita()



while True:
    bola.move()
    pantalla.update()
    time.sleep(0.01)


pantalla.mainloop()

