#sumar los x primeros numeros cuadrados
import os
h=int(os.sys.argv[1])

i=0
suma=0
while( i<=h):
    suma +=i*i
    i +=1
#fin_while
print("la suma de los 100 primeros numeros  cuadrados es:", suma)
