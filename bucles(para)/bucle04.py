import os
g=int(os.sys.argv[1])
o=int(os.sys.argv[2])
g_invalido=(g<0 or g>15)
o_invalido=(o<0 or o>15)

while(g_invalido ==True):
    g=int(input("ingrese promedio01:"))
    g_invalido=(g<0 or g>15)
while(o_invalido ==True):
    o=int(input("ingrese promedio02 :"))
    o_invalido=(o<0 or o>15)
coleccion={"carlos":g ,"andres":o , }
print("nombe", "      promedio_total")
for i in coleccion:
    print(i,"->", coleccion[i])
