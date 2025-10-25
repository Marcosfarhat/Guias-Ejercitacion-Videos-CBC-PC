# Comportamiento 1
# Borra
'''
archivo=open('archivo.txt','w+')
lineas=archivo.readlines()
print()
archivo.close()
'''

# Comportamiento 2
#
'''
archivo=open('archivo.txt','w+')
archivo.write('linea nueva')
archivo.close()
 '''

# Comportamiento 3
#
'''archivo=open('archivo.txt','w+')
lineas=archivo.read()
archivo.write('linea nueva')
# imprime la representacion del objeto
print(archivo)
archivo.close()
'''

