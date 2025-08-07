def menu(opciones):
    ''' arma menú de opciones y devuelve selección entera
    recibe tupla con opciones de menú'''
    print('Selecciona una opción')
    for i in range(1,len(opciones)):
        print(i,'-' , opciones[i])
    opc=int(input())
    while opc not in range(1,len(opciones)):
        opc=int(input())
    return opc

# Secuencias, Tuplas y Listas APUNTE DE CÁTEDRA

panes=('','semilla','arabe')
carnes=('','hamburguesa')
quesos=('','cheda')
acomp=('','tomate')
salsas=('','mayonesa')

print('Armá tu sandwich')
op1=menu(panes)
op2=menu(carnes)
op3=menu(quesos)
op4=menu(acomp)
op5=menu(salsas)
print('Tu pedido de sandwich de pan',panes[op1],'saldrá pronto')
print('Detalle:',carnes[op2],quesos[op3],acomp[op4],salsas[op5],sep='\n')
