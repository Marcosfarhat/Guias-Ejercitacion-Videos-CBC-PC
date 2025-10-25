diccionario = {
    'a':(10,'marcos','farhat',80),
    'b':(13,'alberto','farhat',70),
    'c':(15,'juan','farhat',20),
}
clave_max = max(diccionario, key=diccionario.get) # 'b'
valor_max = diccionario[clave_max] # 13
print(clave_max)
# print(valor_max)
# print(diccionario)
