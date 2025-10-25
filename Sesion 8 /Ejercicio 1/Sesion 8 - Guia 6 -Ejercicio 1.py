pregunta=open('pregunta.txt','r+')
print(type(pregunta))
lista_pregunta=pregunta.read()

print(lista_pregunta)
respuesta=input()
pregunta.write('\n'+respuesta)
# print(respuesta)
pregunta.close()




# print('antes de escribirl la respuesta',lista_pregunta)
# respuesta=input()
# lista_pregunta.write(respuesta)
# print('Despues de escribir la respuesta',lista_pregunta)
