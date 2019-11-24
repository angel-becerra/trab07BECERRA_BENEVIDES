#sumar los x primeros numeros multiples de 3
import os
m=int(os.sys.argv[1])

i=0
suma=0
while( i<=m):
    suma +=i
    i += 3
#fin_while
print("la suma de los 100 primeros numeros  multiples de 3 es:", suma)
