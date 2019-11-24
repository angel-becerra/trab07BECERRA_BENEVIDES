import os
k=int(os.sys.argv[1])
p=int(os.sys.argv[2])
k_invalido=(k<0 or k>15)
p_invalido=(p<0 or p>15)

while(k_invalido ==True):
    k=int(input("ingrese nota02:"))
    k_invalido=(k<0 or k>15)
while(p_invalido ==True):
    p=int(input("ingrese nota03:"))
    p_invalido=(p<0 or p>15)
coleccion={"roberto":k ,"pedro":p , }
print("nombe", "      promedio")
for i in coleccion:
    print(i,"->", coleccion[i])
