#mostrar mensaje "desea sequir "si o no
import os
precio=int(os.sys.argv[1])

precio_invalido=(precio<0 or precio>85)
while(precio_invalido==True ):
     precio=int(input("ingresa otra precio:"))
     precio_invalido=(precio<0 or precio>85)
#fin_while
print("fin del bucle")
print("el precio es:", precio)

