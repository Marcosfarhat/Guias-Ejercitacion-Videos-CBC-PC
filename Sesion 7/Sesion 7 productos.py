productos={}
cgo=int(input('Ingrese código, 0 para terminar '))
while cgo!=0:
    if cgo not in productos:
         desc=input('Descripción de %d '%cgo)
         unidad=input('Unidad de Medida de %s '%desc)
         precio=float(input('Precio unitario de %s '%desc))
         productos[cgo]=(desc,unidad,precio)
    cgo=int(input('Ingrese código, 0 para terminar el ingreso e ir a la venta '))
#imprime los articulos cargados para mostrarselos y que elija que lleva
for cgo in productos:
    print(cgo,*productos[cgo])
 #termina la carga y comienza el pago total
 #Pregunta cual de los articulos lleva
total=0
cgo=int(input('Qué articulos lleva de los descripto en la parte superior? 0 para ir al costo total  '))
#
while cgo not in productos and cgo!=0:
    cgo=int(input('llevas algo mas? 0 para salir 2'))
while cgo!=0:
    cant=float(input('Cantidad de %s '%(productos[cgo][0])))
    total+=cant*productos[cgo][2]
    cgo=int(input('lleva algun articulo mas? 0 para hacer la suma y dar el total a pagar '))
    while cgo not in productos and cgo!=0:
          cgo=int(input('Qué lleva? 0 para salir 4 '))
print('Debe abonar: $%.2f'%total,sep='')