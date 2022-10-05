from tkinter import *

class Calculadora:
    def __init__(self):
        self.resultado = 0
        # Se introduce valor
    def calcularImporte(self, fruta,peso,tarjeta,tipo_tarj):
        
        if tarjeta == 1:
            if fruta == "Naranjas":
                importe = 2 * peso/1000
                if tipo_tarj == "V":
                    importe += 0.2
                    self.resultado = importe
                else:
                    importe += 0.25
                    self.resultado = importe
            elif fruta == "Limones":
                importe = 1.2 * peso/1000
                if tipo_tarj == "V":
                    importe += 0.2
                    self.resultado = importe
                else:
                    importe += 0.25
                    self.resultado = importe          
            elif fruta == "Manzanas":
                importe = 2.25 * peso/1000
                if tipo_tarj == "V":
                    importe += 0.2
                    self.resultado = importe
                else:
                    importe += 0.25
                    self.resultado = importe
        else:
            if fruta == "Naranjas":
                importe = 2 * peso/1000                
                self.resultado = importe
            elif fruta == "Limones":
                importe = 1.2 * peso/1000
                self.resultado = importe
            elif fruta == "Manzanas":
                importe = 2.25 * peso/1000
                self.resultado = importe     
        
class Ventana:
    def __init__(self, master):
        self.frm = Frame(master, padx = 10, pady = 10)
        self.calculo = Calculadora()
        ######LISTA DESPLEGABLE######..
        # Variable de control
        self.opcion = StringVar()
        # Declaracion del componente con las opciones a mostrar
        self.w = OptionMenu(master, self.opcion, "Naranjas", "Limones", "Manzanas")
        self.w.pack()
        # Valor predeterminado seleccionado
        self.opcion.set("Elija la fruta...")
        #######SPINBOX#######
        # Variable de valor para el spinbox
        self.valor = IntVar()
        self.sp = Spinbox(master, from_=100, to=5000,  textvariable=self.valor)
        self.sp.pack()
        self.valor.set(100)
        Button(master, text="REINICAR VALOR", command=self.fijar).pack()
        ####CHECK BUTTOn####
        self.estado = IntVar()
        self.c = Checkbutton(master, text="Tarjeta de crédito", variable=self.estado, command=self.activar)
        self.c.pack()
        ###VISA O MASTERCARD###
        self.tarjeta = StringVar()
        self.visa=Radiobutton(master, text="Visa", variable=self.tarjeta, value = "V",state=DISABLED)
        self.master=Radiobutton(master, text="Mastercard", variable=self.tarjeta, value = "M",state=DISABLED)
        self.visa.pack()
        self.master.pack()
        ##BOTON###
        self.boton = Button(master, text="Confirmar pedido")
        self.boton.bind("<Button-1>", self.clic)
        self.boton.pack()
        ##ETIQUETA #####
        self.etiqueta = Label(master, text = "0",padx = 10, pady=10,)
        self.etiqueta.pack()

    def fijar(self):
        self.valor.set(100)
        
    def activar(self):
        if self.estado.get() == 1:
            self.visa.config(state=NORMAL)
            self.master.config(state=NORMAL)
        else:
            self.visa.config(state=DISABLED)
            self.master.config(state=DISABLED)
            
    def clic(self,ev):
        fruta = self.opcion.get()
        peso = self.valor.get()
        tarjeta = self.estado.get()
        tipo_tarj= self.tarjeta.get()
        self.calculo.calcularImporte(fruta,peso,tarjeta,tipo_tarj)
        self.etiqueta.config(text=str(self.calculo.resultado))
       
def main():
    root = Tk()
    root.title("Aplicacion")
    root.geometry("540x250")
    Ventana(root)
    root.mainloop()

main()
