nombres=open('regalo.txt','r+')
nombre_pasado_a_cadena = nombres.readlines()
print(nombre_pasado_a_cadena)
cont=0
for i in range(len(nombre_pasado_a_cadena)):
     nombre_pasado_a_cadena[i]=nombre_pasado_a_cadena[i].strip('\n')
     cont+=1
for i in nombre_pasado_a_cadena:
     if i == 'santi':
          print(i)
          nombres.write('tomi')


print(nombre_pasado_a_cadena)
print('total recaudado', 1000*cont)
nombres.close()




# def plata(nom):
#    cont=0
#    for i in nom:
#        print(i)
#        cont+=1
#    return (cont*1000)
#
# print(plata(nom1))
