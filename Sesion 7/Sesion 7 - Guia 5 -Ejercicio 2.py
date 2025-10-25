plantas=[]

def planta_nueva(especie,luz,precio):
    planta ={especie,luz,precio}
    plantas.append(planta)
    return plantas


especie=input('ingrese la planta')
luz=bool(input('necesita luz si=1/no=0'))
precio=float(input('precio '))
plantas=planta_nueva(especie,luz,precio)
print(plantas)
