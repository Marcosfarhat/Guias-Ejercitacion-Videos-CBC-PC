# 1 Comportamiento 1
# archivo=open('archivo.txt','r+')
# lineas=archivo.readlines()
# print(lineas)
# archivo.close()
#
# # Comportamiento 2
# archivo=open('archivo.txt','r+')
# archivo.write('Texto nuevo que pisa al anterior pero solamente la seccion que escribo aca ')
# # readlineas intenta leer desde la posicion actual del cursor o sea que si no hay nada despues de "...escribo aca"
# # no muestra ningun texto
# lineas=archivo.readlines()
# print(lineas)
# archivo.close()

#   COMPORTAMIENTO 3/ Lectura y Escritura
# readlinea + write no importa su orden, WRITE lo agrega al final de la posicion del cursor
archivo=open('archivo.txt','r+')
lineas=archivo.readlines()
print(lineas)
archivo.write('Texto nuevo que suma al anterior , para ejemplo  de .readlines primero y despues .write ')
archivo.close()
# -----------------

