def guardar():
    materias=[]
    materia = input('Ingresa la materia que deseas almacenar')
    while (materia != 'x'):
        materias.append(materia)
        materia = input('Ingresa la materia que deseas almacenar')
    print('se termino y te imprimo lo que almacenamos hasta ahora', materias)

guardar()

