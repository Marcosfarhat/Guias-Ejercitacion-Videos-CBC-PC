from dataclasses import replace
from operator import index

print('Practica de hacer una lista y cambiar un elemento')
'''print('--------------------')
print('lista 1')
list_1 = ['carlos','eugenio',]
cambio_de_nombre = list_1.index('eugenio')
# cambio_de_nombre guarda el lugar 1 (0 = al primner lugar , 1= al segundo lugar ' eugenio'
list_1[cambio_de_nombre]='juan'
# list_1.replace['eugenio','juan']
print(list_1)'''

# print('---------------')
# Actividad ejercicio 6
# a
# lista_2=['Alberta',' Juana',' Mariana','Marcela', 'Carla']
# paso el elemento Carla ( que voy a cambiar por juan) a cambio_por_juan
# cambio_por_juan = lista_2.index('Carla')
# cambio por juan a Carla, que esta en la variable cambio_por_juan
# lista_2[cambio_por_juan]='juan'
# print(lista_2)

print('---------------------')
# lista_2=['Alberta',' Juana',' Mariana','Marcela', 'Carla']
# print('busco el ultimo elemento (numero de posicion) y lo reemplazo sabiendo su ubicacion(numero de posicion')
# print('Utilizo la variable len() para saber la cantidad de elemntos e insert() para agregarlo')
# como saber cuantos elementos tiene una lista
# le paso el numero a cant_de_elementos_lista_2
# cant_de_elementos_lista_2 = len(lista_2)
# lo inserta por no reemplaza a carla
# lista_2.insert(cant_de_elementos_lista_2-1,'juan')
# print(lista_2)

print('---------------------')
# probamos replace en strings
print('Probamos replace()')
lista_2=['Alberta',' Juana',' Mariana','Marcela', 'Carla']
# paso el dato 5 -Carla
ultimo_nombre = lista_2[4]
# print(ultimo_nombre)
print('---------------------')
# otra forma de buscar el ultimo elemento
# ultimo_nombre_2= lista_2[-1]
# print(ultimo_nombre_2)
# num=1
# print(lista_2[5-1])
print('---------------------')
# paso la lista reemplazada a una lista nueva
lista_2=[p.replace(ultimo_nombre,'juan')for p in lista_2]
print(lista_2)

# lista_2_reemplaza_nueva = [lista_2.replace(cant_de_elementos_lista_2,'juan')







'''reemplazar = lista_2.index('Carla')
lista_2[reemplazar] = 'Carlota'
print(lista_2)
print('---------------')
print('lista 3')
lista_3=['chachi','pochi','lucho','titi']
busco = lista_3.index('titi')
lista_3[busco]= 'toto'
print(lista_3)
print('---------------')
print('lista 4')
lista_4=['juan','pedro']
busco_4=lista_4.index('pedro')
lista_4[busco_4]='cacho'
print(lista_4)
print('---------------')
print('lista 5')
lista_5=['pedro','carlos']
busco_5=lista_5.index('carlos')
# busco_5 guarda el lugar, el index del elemento en este caso el 0 por que es el primer elemento
print(type(busco_5))
print(busco_5)
valos_nuevo = busco_5 + 1 + busco_5
print(valos_nuevo)
lista_5[busco_5]='cachito'
print('---------------')'''

