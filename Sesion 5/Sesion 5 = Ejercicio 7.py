lista_tupla=[(1,'cocinar'),(2,'lavar'),(3,'barrer'),(4,'planchar')]
tarea_manuel_acumuladas=[]
lista_acum_descripcion= []
for i in lista_tupla:
    segundo = i[0]
    if segundo %2 == 0:
        tarea_manuel = segundo
        # print(f'las tareas de manuel son las {tarea_manuel}')
        tarea_manuel_acumuladas.append(tarea_manuel)
        # print('tareas acumuladas',tarea_manuel_acumuladas)
# print('tareas acumuladas',tarea_manuel_acumuladas)
for i in tarea_manuel_acumuladas:
    lista_acum_descripcion.append(lista_tupla[i-1])
    # print('descripcion',lista_acum_descripcion)

print('final;',lista_acum_descripcion )

