# funcion siempre primero
def promedio(notas):
    notas_total=0
    cantidad=0
    # nota_estudiante itera cada diccionario
    for nota_estudiante in notas:
        # print(nota_estudiante['Intentos'])
        if nota_estudiante['Intentos']==1:
            cantidad+=1
            notas_total=notas_total+nota_estudiante['Nota']
            # print(notas_total)
    prom=notas_total/cantidad

    return prom

nota=[
    {'Nombre':'Juan','Apellido':'Saravia','Intentos':1,'Nota':10},
    {'Nombre':'Pedro','Apellido':'Lorezo','Intentos':2,'Nota':9},
    {'Nombre':'Smith','Apellido':'Garcia','Intentos':1,'Nota':8}
]
print(promedio(nota))
