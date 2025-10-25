# alias=open('anioralgias.txt')
# Creacion de un archivo y le agregamos elementos
# Opcion 1
from fileinput import close

archivo=open('archivo.txt','w')
archivo.write('este es un texto previo\n')
archivo.write('este tambien\n')
archivo_escrito=archivo
archivo.close()

# Opcion 2
archivo1=open('archivo_1.txt','w')
archivo1.writelines(['hola','adios'])
archivo1.writelines('chau')
archivo1.close()

# Append
archivo_append= open('archivo.txt','a')
archivo_append.writelines(['hola','\nchau'])
archivo_append.writelines(['\nchau'])
archivo_append.close()

# agregar en MODO 'r' --> si no exite da error
# En estos ejemplos el archivo por defecto existe
archivo1_r_plus= open('archivo.txt','r+')
lineas=archivo1_r_plus.readlines()
print(lineas)
archivo1_r_plus.close()
