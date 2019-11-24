import os
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])
l=int(os.sys.argv[3])
m_invalido=(m<0 or m>15)
n_invalido=(n<0 or n>15)
l_invalido=(l<0 or l>15)
while(m_invalido==True):
    m=int(input("ingrese nota01:"))
    m_invalido=(m<0 or m>15)
while(n_invalido==True):
    n=int(input("ingrese nota02:"))
    n_invalido=(n<0 or n>15)
while(l_invalido==True):
    l=int(input("ingrese nota03:"))
    l_invalido=(l<0 or l>15)
coleccion={"aleja":m ,"homar":n , "alber":l}
print("nombre", "      nota_del_examen")
for i in coleccion:
    print(i,"->", coleccion[i])
