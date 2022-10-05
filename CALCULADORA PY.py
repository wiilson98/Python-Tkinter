from tkinter import *


class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.operacion = None
        # Se introduce valor
    def valor(self, valor):
        if self.operacion == None:
            self.resultado = valor
        elif self.operacion == "+":
            self.resultado = self.resultado + valor
        elif self.operacion == "-":
            self.resultado = self.resultado - valor
        elif self.operacion == "/":
            self.resultado = self.resultado / valor
        elif self.operacion == "x":
            self.resultado = self.resultado * valor
        # Se introduce operador
    def operador(self, op):
        self.operacion = op
            # Reinicio de la calculadora
    def reinicio(self):
        self.resultado = 0
        self.operacion = None

class MainFrame():
    def __init__(self, parent):
        self.frm = Frame(parent, padx = 10, pady = 10)
        self.frm.pack( fill = BOTH, expand = True)
        # Instancia del objeto Calculadora
        self.calculadora = Calculadora()
        # Generacion de los componentes boton
        valores = [ ["7", "8", "9", "/"],["4", "5", "6", "x"],["1", "2", "3", "-"],["R", "0", "=", "+"]]
        for fila in range(0,4):
            for col in range(0,4):
                self.btn = Button(self.frm, text=valores[fila][col])
                self.btn.bind("<Button-1>", self.clic)
                self.btn.place(relx = 0.25 * col, rely = 0.2 * (fila+1),relwidth = 0.25, relheight = 0.25)
        # Componente etiqueta
        self.lbl = Label(self.frm, text = "", anchor = E, borderwidth = 3, relief =SUNKEN )
        self.lbl.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
    # Método manejador para todos los botones
    def clic(self, ev):
        boton = ev.widget["text"]
        if boton == "+" or boton == "-" or boton == "x" or boton == "/":
            # El boton pulsado es un operador.
            self.calculadora.valor(int(self.lbl["text"]))
            self.calculadora.operador(boton)
            self.lbl.config(text = "") # Limpia la etiqueta
        elif boton == "=":
            # El boton pulsado es el igual
            self.calculadora.valor(int(self.lbl["text"]))
            self.lbl.config(text = str(self.calculadora.resultado))
            self.calculadora.reinicio()
        elif boton == "R":
            # El boton pulsado es el de reinicio
            self.calculadora.reinicio()
            self.lbl.config(text = "") # Limpia la etiqueta
        else:
            # El boton pulsado es un numero.
            # Concatena el valor indicado a la etiqueta
            valor = self.lbl["text"] + ev.widget["text"]
            self.lbl.config(text = valor)

if __name__ == "__main__":
    root = Tk()
    root.title("Aplicacion")
    root.geometry("320x240")
    # Instanciacion de Frame principal
    MainFrame(root)
    # Inicio de ejecución
    root.mainloop()
