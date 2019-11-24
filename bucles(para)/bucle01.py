#impresion de los promedios de los alumnos
import os
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
f=int(os.sys.argv[3])
x_invalido=(x<0 or x>15)
y_invalido=(y<0 or y>15)
f_invalido=(f<0 or f>15)
while(x_invalido==True):
    x=int(input("ingrese nota01:"))
    x_invalido=(x<0 or x>15)
while(y_invalido==True):
    y=int(input("ingrese nota02:"))
    y_invalido=(y<0 or y>15)
while(x_invalido==True):
    y=int(input("ingrese nota03:"))
    y_invalido=(f<0 or f>15)
coleccion={"alejandro":x ,"juana":y , "alberto":f}
print("nombe", "      promedio")
for i in coleccion:
    print(i,"->", coleccion[i])
