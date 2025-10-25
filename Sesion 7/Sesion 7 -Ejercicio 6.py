def elem_eliminados(producto):
    excomulgados = []
    contador=0
    cont_exco=0
    quedaron=0
    for dic in producto:
        contador+=1
        # print(dic)
        if dic['Chequeado']==False:
            cont_exco+=1
            excomulgados.append(dic)
            # print('estamos en excomulgados',excomulgados)
    quedaron=contador-cont_exco
    tupla=tuple(excomulgados)
    return tupla,quedaron
productos=[
    {'codigo':1,'Vencimiento':'3/5/25','Chequeado':True},
    {'codigo':3,'Vencimiento':'12/5/25','Chequeado':False},
    {'codigo':2,'Vencimiento':'6/5/25','Chequeado':False}

]
# print(elem_eliminados(productos))
tupla=elem_eliminados(productos)
tupla_sola=tupla[0]
quedaron=tupla[1]
print( tupla_sola)
print( quedaron)

