#mostrar mensaje "clave invalida "si la clave ingresada no es 1234
import os
clave=int(os.sys.argv[1])

clave_invalida=( clave != 1234)
while(clave_invalida==True ):
     clave=int(input("ingresa otra clave:"))
     clave_invalida=( clave != 1234)
#fin_while
print("fin del bucle")
print("la clave es:", clave)
