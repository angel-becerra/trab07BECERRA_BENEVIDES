#mostrar mensaje "desea sequir "si o no
import os
edad=int(os.sys.argv[1])

edad_invalida=(edad<0 or edad>100)
while(edad_invalida==True ):
     edad=int(input("ingresa otra edad:"))
     edad_invalida=(edad<0 or edad>100)
#fin_while
print("fin del bucle")
print("la edad es:", edad)
