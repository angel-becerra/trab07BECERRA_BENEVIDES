#sumar los x primeros numeros multiples de 7
import os
k=int(os.sys.argv[1])

i=0
suma=0
while( i<=k):
    suma +=i
    i += 7
#fin_while
print("la suma de los 100 primeros numeros  multiples de 7 es:", suma)

