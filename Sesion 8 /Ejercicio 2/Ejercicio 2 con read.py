def plata_regalo():
    
nombres=open('regalo.txt','r+')
# read crea uina cadena de texto
nombre_pasado_a_cadena = nombres.read()
print(nombre_pasado_a_cadena)
# nombre_pasaado_a_cadena_2=nombre_pasaado_a_cadena.replace('\n',' ')
nombres.close()