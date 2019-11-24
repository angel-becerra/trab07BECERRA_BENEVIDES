#mostrar mensaje "desea sequir "si o no
import os
mes_del_año=os.sys.argv[1]


mes_invalido=True
while(mes_invalido):
     mes=input("ingresa otro mes enero/febrero/marzo/abril/mayo/junio/julio/agosto/setiembre/octubre/noviembre/diciembre:")
     mes_invalido=(mes_del_año!="enero" and mes_del_año !="febrero" and mes_del_año !="marzo" and mes_del_año !="abril" and mes_del_año !="mayo" and mes_del_año !="junio" and mes_del_año !="julio" and mes_del_año !="agosto" and mes_del_año !="setiembre" and mes_del_año!="octubre"and  mes_del_año !="noviembre" and mes_del_año !="diciembre")

#fin_while
print("fin del bucle")
print("el mes del año  es:", mes_del_año)
