from tkinter import *
class Botonera:
    def __init__(self, parent, container):
        # Referencia al contenedor de la ventana principal
        self.container = container
        # Referencia a la propia ventana principal
        self.parent = parent
        # Creacion del contenedor para esta ventana
        self.top = Toplevel(container)
        self.top.transient(container)
        self.top.title("Botonera")
        # Posicionamiento con respecto a la ventana principal
        self.top.geometry("200x200+%d+%d" % (container.winfo_rootx()-220,container.winfo_rooty()-30))
        # Generacion de los componentes boton
        self.botones=[]##############
        valores = [ ["7", "8", "9", "/"],["4", "5", "6", "x"],["1", "2", "3", "-"],["R", "0", "=", "+"]]
        for fila in range(0,4):
            for col in range(0,4):
                self.btn = Button(self.top, text=valores[fila][col])
                self.btn.bind("<Button-1>", self.pulsacion)
                self.btn.place(relx = 0.25 * col, rely = 0.25 * fila, relwidth = 0.25,relheight = 0.25)
                self.botones.append(self.btn)########
    # Funcion manejadora de pulsacion de botones
    def pulsacion(self, event):
        print(event.widget['text'])
        self.parent.mostrar(event.widget['text'])
    def bloquear(self):
        # Recorre la lista de botones modificando estado a DISABLED
        for btn in self.botones:
            btn.config(state = DISABLED)
    def desbloquear(self):
        # Recorre la lista de botones modificando estado a NORMAL
        for btn in self.botones:
            btn.config(state = NORMAL)
class Ventana:
    def __init__(self, container):
        self.container = container
        # Definicion de la etiqueta para mostrar los valores
        self.display = Label(self.container, text="", font=("Arial", 40))
        self.display.pack(side=RIGHT)
        # Instanciacion de la ventana botonera para que se muestre
        self.botonera = Botonera(self, container)
        # Botones de bloqueo y desbloqueo
        Button(self.container, text="Bloquear botonera",command=self.botonera.bloquear).pack(side=LEFT)
        Button(self.container, text="Desbloquear botonera",command=self.botonera.desbloquear).pack(side=LEFT)

        
    def mostrar( self, value):
        self.display['text'] = self.display['text'] + value

        
def main():
    root = Tk()
    root.title("Calculadora")
    root.geometry("640x100+500+500")
    root.update()
    Ventana(root)
    root.mainloop()
main()
