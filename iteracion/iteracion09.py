#producto los x primeros numeros pares
import os
q=int(os.sys.argv[1])

i=2
producto=2
while( i<=q):
    producto *=i
    i +=2
#fin_while
print("la producto de los 10 primeros numeros  pares es:", producto)
