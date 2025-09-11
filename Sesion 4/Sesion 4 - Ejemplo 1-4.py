#Ej de carga e impresión de listas
nombres=[]
nom=input('Ingrese un nombre, * para salir: ')
while nom !='*':
    nombres.append(nom)
    nom=input('Ingrese un nombre, * para salir:')
    print(nombres)
print('Lista de Nombres')
print(nombres)
print('Salida detallada')
for n in nombres:
    print(n)