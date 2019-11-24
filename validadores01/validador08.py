#mostrar mensaje "desea sequir "si o no
import os
sexo=os.sys.argv[1]

sexo_no_valido=True
while(sexo_no_valido):
     sexo=input("tipo de sexo es:")
     sexo_no_valido=(sexo !="masculino" and sexo != "femenino")
#fin_while
print("fin del bucle")
print("el sexo es:", sexo)
