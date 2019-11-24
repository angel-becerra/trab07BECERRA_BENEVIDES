#sumar los y primeros numeros pares
import os
y=int(os.sys.argv[1])

i=0
suma=0
while( i<=y):
    suma +=i
    i += 2
#fin_while
print("la suma de los 100 primeros numeros  pares es:", suma)
