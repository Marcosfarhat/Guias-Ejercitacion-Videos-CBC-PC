def menu(opciones):
    ''' arma menú de opciones y devuelve selección entera
    recibe tupla con opciones de menú'''
    print('Selecciona una opción')
    for i in range(1,len(opciones)):
        # i=i-1
        # print(i)
        print(i,'-' , opciones[i][0])

    opc=int(input())
    while opc not in range(1,len(opciones)):
        opc=int(input())
    return opc
# Secuencias, Tuplas y Listas APUNTE DE CÁTEDRA
panes=(' ', ('arabe',70),
       ('pebete',70,2),
       ('france',60,3),
       ('france2',60,3))
carnes=('',('hamburguesa',200),
        ('jamon cocido',150),
        ('lomito',199),
        ('lomit_1',199))
quesos=('',('chedar',75),
        ('dambo',60),
        ('sin queso',0))

print('Armá tu sandwich')
sand=[]
op1=menu(panes)
sand.append(panes[op1][1])
op2=menu(carnes)
sand.append(carnes[op2][1])
op3=menu(quesos)
sand.append(quesos[op3][1])
print('Tu pedido de sandwich de pan',panes[op1][1],'saldrá pronto')
print('Detalle:',carnes[op2],quesos[op3][0],sep='\n')
print(('Abonarr: $%.2f'%sum(sand)))
