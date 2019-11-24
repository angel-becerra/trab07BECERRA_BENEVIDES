#mostrar mensaje "numero_usuario_invalido" si el  numero de usuario no es 45879
import os
numero_de_usuario=int(os.sys.argv[1])

numero_de_usuario_invalido=( numero_de_usuario != 45879)
while(numero_de_usuario_invalido==True ):
     numero_de_usuario=int(input("ingresa otro codigo:"))
     numero_de_usuario_invalido=( numero_de_usuario != 45879)

#fin_while
print("fin del bucle")
print("el numero de usuario es es:", numero_de_usuario)
