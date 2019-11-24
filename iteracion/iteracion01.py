#sumar los x primeros numeros pares
import os
x=int(os.sys.argv[1])

i=0
suma=0
while( i<=x):
    suma +=i
    i += 1
#fin_while
print("la suma de los 100 primeros numeros es:", suma)
