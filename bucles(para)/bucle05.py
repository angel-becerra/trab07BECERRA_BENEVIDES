import os
a=int(os.sys.argv[1])
w=int(os.sys.argv[2])
a_invalido=(a<0 or a>15)
w_invalido=(w<0 or w>15)

while(a_invalido ==True):
    a=int(input("ingrese nota02:"))
    a_invalido=(a<0 or a>15)
while(w_invalido ==True):
    w=int(input("ingrese nota03:"))
    w_invalido=(w<0 or w>15)
coleccion={"roberto":a ,"pedro":w }
print("nombe", "      promedio")
for i in coleccion:
    print(i,"->", coleccion[i])
