#decodoficar mensaje incriptado
import os

#input
ARGUMENTO=os.sys.argv[1].upper()
#bucle
for letra in ARGUMENTO:
 if letra == "A":
    print(" LISTA DE COMPRAS:")
 if letra == "R":
    print("FRUTAS:MANZANA,PERA,MANDARINA ")
 if letra == "G":
    print("VERDURAS:BROCOLI,TOMATE")
 if letra == "U":
    print("CARNE:POLLO,PAVITO")
 if letra == "M":
    print("CONDIMENTOS:COMINO,SIBARITA")
 if letra == "E":
    print("DULCES:TRANCA,ALFAJOR")
 if letra == "N":
    print("BEBIDAS:GASEOSA,PUL")
 if letra == "T":
    print("TOTAL:159")
 if letra == "O":
    print("GRACIAS POR LA COMPRA")


#fin_iterar
print("\n")
print("fin del bucle")
