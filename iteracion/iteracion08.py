#producto los x primeros numeros
import os
g=int(os.sys.argv[1])

i=1
producto=1
while( i<=g):
    producto *=i
    i +=1
#fin_while
print("la producto de los 100 primeros numeros es:", producto)
