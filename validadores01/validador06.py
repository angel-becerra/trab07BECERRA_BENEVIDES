#mostrar mensaje "codigo no soportado"si la clave ingresada no es 1234
import os
codigo=int(os.sys.argv[1])

codigo_invalido=( codigo != 745484)
while(codigo_invalido==True ):
     codigo=int(input("ingresa otro codigo:"))
     codigo_invalido=( codigo != 745484)
#fin_while
print("fin del bucle")
print("el codigo es:", codigo)
