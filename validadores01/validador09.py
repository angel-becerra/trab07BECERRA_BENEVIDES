#mostrar mensaje "desea sequir "si o no
import os
total_alumnos=int(os.sys.argv[1])

alumnos_no_inscritos =(total_alumnos<0 or total_alumnos>85)
while(alumnos_no_inscritos==True ):
     alumnos=int(input("ingresa otra cantidad:"))
     alumnos_no_inscritos=(total_alumnos<0 and total_alumnos>100)
#fin_while
print("fin del bucle")
print("el total de alumnos es:", total_alumnos)
