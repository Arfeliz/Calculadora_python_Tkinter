from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
 
i = 0

#entrada de datos
e_texto = Entry(ventana, font=("calibri 20"))
e_texto.grid(row=0, column= 0, columnspan= 4, padx= 5, pady= 5 )


#Botones

boton1 = Button(ventana, text= "1", width=5, height=2, command= lambda : click_boton(1))
boton2 = Button(ventana, text= "2", width=5, height=2, command= lambda : click_boton(2))
boton3 = Button(ventana, text= "3", width=5, height=2, command= lambda : click_boton(3))
boton4 = Button(ventana, text= "4", width=5, height=2, command= lambda : click_boton(4))
boton5 = Button(ventana, text= "5", width=5, height=2, command= lambda : click_boton(5))
boton6 = Button(ventana, text= "6", width=5, height=2, command= lambda : click_boton(6))
boton7 = Button(ventana, text= "7", width=5, height=2, command= lambda : click_boton(7))
boton8 = Button(ventana, text= "8", width=5, height=2, command= lambda : click_boton(8))
boton9 = Button(ventana, text= "9", width=5, height=2, command= lambda : click_boton(9))
boton0 = Button(ventana, text= "0", width=15, height=2, command= lambda : click_boton(0))

boton_borrar = Button(ventana, text= "AC", width=5, height=2 )
boton_parentesos1 = Button(ventana, text= "(", width=5, height=2, command= lambda : click_boton("("))
boton_parentesos2 = Button(ventana, text= ")", width=5, height=2, command= lambda : click_boton(")"))

boton_suma = Button(ventana, text= "+", width=5, height=2, command= lambda : click_boton("+"))
boton_resta = Button(ventana, text= "-", width=5, height=2, command= lambda : click_boton("-"))
boton_multiplicacion = Button(ventana, text= "*", width=5, height=2, command= lambda : click_boton("*"))
boton_division = Button(ventana, text= "/", width=5, height=2, command= lambda : click_boton("/"))
boton_igual = Button(ventana, text= "=", width=5, height=2 )
boton_punto = Button(ventana, text= ".", width=5, height=2, command= lambda : click_boton("."))

#agregar botones
boton_borrar.grid(row=1 , column=0 , padx=5, pady=5 )
boton_parentesos1.grid(row=1 , column=1 , padx=5, pady=5 )
boton_parentesos2.grid(row=1 , column=2 , padx=5, pady=5 )
boton_division.grid(row=1 , column=3 , padx=5, pady=5 )

boton7.grid(row=2 , column= 0, padx=5, pady= 5)
boton8.grid(row=2, column= 1, padx=5, pady=5 )
boton9.grid(row=2 , column= 2, padx=5, pady=5 )
boton_multiplicacion.grid(row=2 , column=3 , padx=5, pady=5 )

boton4.grid(row=3 , column= 0, padx=5, pady=5 )
boton5.grid(row=3 , column= 1, padx=5, pady= 5)
boton6.grid(row=3 , column= 2, padx=5, pady= 5)
boton_resta.grid(row=3 , column=3 , padx=5, pady=5 )

boton1.grid(row=4 , column= 0, padx=5, pady=5 )
boton2.grid(row=4 , column= 1, padx=5, pady= 5)
boton3.grid(row=4 , column= 2, padx=5, pady=5 )
boton_suma.grid(row=4 , column=3 , padx=5, pady=5 )

boton0.grid(row=5 , column=0 , columnspan=2, padx=5, pady=5 )
boton_punto.grid(row= 5, column=2 , padx=5, pady=5 )
boton_igual.grid(row= 5, column=3 , padx=5, pady=5 )
ventana.mainloop()