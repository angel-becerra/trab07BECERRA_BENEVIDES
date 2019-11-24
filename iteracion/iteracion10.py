#producto los x primeros numeros cuadrados
import os
d=int(os.sys.argv[1])

i=1
producto=1
while( i<=d):
    producto *=i*i
    i +=1
#fin_while
print("el producto de los 10 primeros numeros  cuadrados es:", producto)
