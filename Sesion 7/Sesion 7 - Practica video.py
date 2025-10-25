diccionario={'hola':12, 'chau':2}
# print(diccionario['hola'])
# diccionario.update({'agrego':(1,2,3,3)})
# diccionario.update({'hola': {'1983,medicina'}})
diccionario2={'gato':23}
diccionario['diccionario2']=diccionario2
print(*diccionario)
print(diccionario)
for i in diccionario:
    print(i,diccionario[i])
# for i in diccionario:
#     print(i,diccionario[i])
valor_max= max(diccionario,key=diccionario.get)