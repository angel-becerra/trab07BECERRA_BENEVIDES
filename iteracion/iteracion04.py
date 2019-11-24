#sumar los x primeros numeros multiples de 5
import os
p=int(os.sys.argv[1])

i=0
suma=0
while( i<=p):
    suma +=i
    i += 5
#fin_while
print("la suma de los 100 primeros numeros  multiples de 5 es:", suma)
