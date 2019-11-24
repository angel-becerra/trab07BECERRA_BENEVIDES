#sumar los x primeros numeros cubos
import os
w=int(os.sys.argv[1])

i=0
suma=0
while( i<=w):
    suma +=i*i*i
    i +=1
#fin_while
print("la suma de los 10 primeros numeros  cubos es:", suma)
