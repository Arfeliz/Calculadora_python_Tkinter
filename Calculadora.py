from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

#entrada de datos
e_texto = Entry(ventana, font=("calibri 20"))
e_texto.grid(row=0, column= 0, columnspan= 4, padx= 5, pady= 5 )


ventana.mainloop()