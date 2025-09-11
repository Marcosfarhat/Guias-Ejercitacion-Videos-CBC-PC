listas=[("detergente",123),("Coco",324)]

def funcion (y):
    segunda_variable=[]
    for i in y:
       segundo = i[1]
       segunda_variable.append(segundo)
    return segunda_variable


resultado = funcion(listas)
print(resultado)