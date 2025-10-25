print(' Comportamiento 4- with open as , mantiene el archivo abierto dentro del ambito -with open as- ')
print(' --------------------')
# Despues de leer el archivo todos los tipos de read dejan el cursor al final
with open('archivo.txt','r') as archivo:
    lineas_readline=archivo.readline()
    lineas_read=archivo.read()
    lineas_readlines=archivo.readlines()
    # readline() no lee nada por que el cursor quedo al final
    print(lineas_readline)
    print(lineas_read)
    print(lineas_readlines)
