# completo=open('datosCompletos.csv','w')
# b=[]
# dat=open('datos1.csv')
# a=dat.readlines()
# dat.close()
with open('datos2.csv', 'r') as archivo:
    lineas = archivo.readlines()
    print(lineas)
    print(type(lineas))

# Limpiar y mostrar cada línea como string
lineas_limpias = [linea.strip().split(';') for linea in lineas]
print('lineas',lineas_limpias)

#
# for i in range(len(a)):
#     print(i)
#     campos = a[i].strip().split(',')
# #     a[i]=a[i].strip('\n')
# #     a[i]=a[i].strip(',')
# # #     # a[i][3]=int(a[i][3])
#
# print(campos)

