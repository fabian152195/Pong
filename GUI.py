from tkinter import *

def menuPads(modo):

    root.withdraw()
    inicio = Toplevel()
    inicio.title("Menu")
    inicio.minsize(800, 500)
    inicio.resizable(width=NO, height=NO)
    contenedor_principal = Canvas(inicio, width=800, height=500, bg="gray")


    # Dibujar lineas en el canvas
    # canvas.create line(Xinicio,Yinicio,Xfinal,Yfinal, fill=ColorLInea,dash=(,)
    # canvas.create_text(150,50,text="Hola BIenvenidos", font = ("Times New Roman","18"),anchor =NW)
    # canvas.create_text(150,100,text="Computadores 2018", font = ("Times New Roman","18"),anchor =NW)

    def Juego(modo,c_pads):
        inicio.withdraw()
        ventanaJuego = Tk()
        ventanaJuego.title('Juego')
        ventanaJuego.minsize(800, 500)
        ventanaJuego.resizable(width=NO, height=NO)
        canvaVJuego = Canvas(ventanaJuego, width=800, height=500, bg="gray")



        canvaVJuego.place(x=-3,y=-3)
        ventanaJuego.mainloop()

    def mainMenu():
        root.deiconify()
        inicio.destroy()

    botonA = Button(inicio, width=40, height=10, command= lambda: Juego(modo,1), text="1 PAD")
    botonA.place(x=50, y=280)
    botonB = Button(inicio, width=40, height=10, command=lambda: Juego(modo,2), text="2 PAD")
    botonB.place(x=360, y=280)
    botonBack = Button(inicio, width=8, command=mainMenu, text="Back")
    botonBack.place(x=620, y=460)

    contenedor_principal.place(x=-3, y=-3)
    contenedor_principal.create_image(0, 0, anchor=NW, image=ImgApp1)

    inicio.mainloop()



def mainMenu():
    root.destroy()


root = Tk()
root.title("PONG")
root.minsize(800, 500)
root.resizable(0, 0)
contenedor_Main = Canvas(root, width=800, height=500, bg="gray")
contenedor_Main.place(x=-3, y=-3)



ImgApp1 = PhotoImage(file="fondo1.gif")

contenedor_Main.create_image(0, 0, anchor=NW, image=ImgApp1)

ImgApp2 = PhotoImage(file="PvP.gif")
img_reducidaApp2 = ImgApp2.subsample(1, 1)


#ImgFabi.bind(('<Double-Button-1>', menuPads(1))

buttonA = Button(root, image=img_reducidaApp2, command= lambda: menuPads(1), text="Player vs Player")
buttonA.place(x=100, y=185)
buttonB = Button(root, width=28, height=12, command= lambda: menuPads(2), text="Player vs Computer")
buttonB.place(x=380, y=187)
buttonD = Button(root, width=10, command=mainMenu, text="Close")
buttonD.place(x=650, y=450)

contenedor_Main.create_rectangle(40, 180, 700, 400, fill='white')

root.mainloop()
