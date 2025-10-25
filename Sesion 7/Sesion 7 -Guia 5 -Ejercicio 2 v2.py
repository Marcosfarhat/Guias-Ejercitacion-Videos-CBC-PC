plantas=[]

def planta_nueva():
    ingreso=input('Ingresa de planta 1=si , 2=no ')
    while ingreso !='2':
        if ingreso =='1':
            especie = input('ingrese la planta')
            while True:
                luz_str = input('necesita luz si=1/no=0')
                if luz_str in ('1','0'):
                    luz=(luz_str=='1')
                    break
                else:
                     print('entrada no valida, 1=si 2=no')

            precio = float(input('precio '))
            planta ={
                "especie":especie,
                "luz":luz,
                "precio":precio
            }

            plantas.append(planta)
            ingreso = input('Ingresa de planta 1=si , 2=no ')
        else:
            ingreso = input('Ingresa de planta 1=si , 2=no ')
    return plantas
planta_nueva()
print(plantas)