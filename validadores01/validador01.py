#mostrar mensaje "desea sequir "si o no
import os
respuesta=os.sys.argv[1]

respuesta_invalida=True
while(respuesta_invalida):
     respuesta=input("desea continuar:")
     respuesta_invalida=(respuesta !="si" and respuesta != "no")
#fin_while
print("fin del bucle")
print("la respuesta es:", respuesta)
