# Genera Planilla Integrada de Datos

completo = open('datosCompletos.csv', 'w')
b = []

# Procesar datos1.csv
dat = open('datos1.csv', encoding='latin-1')
a=dat.readlines()
dat.close()
for i in range(len(a)):
    a[i] = a[i].strip('\n')
    a[i] = a[i].split(';')
    a[i][3] = int(a[i][3])
b = b + a
dat = open('datos3.csv', encoding='latin-1')
a=dat.readlines()
dat.close()

for i in range(len(a)):
    a[i] = a[i].strip('\n')
    a[i] = a[i].split(';')
    a[i][3] = int(a[i][3])
b = b + a
# Ordenar por valor descendente y luego por ubicación
b.sort(reverse=True, key=lambda b: (b[3],b[2]))

# Mostrar en pantalla
for elemento in b:
    print(elemento)
    # print(type(elemento))

# Convertir valores a texto y guardar en archivo
# elemento es cada lista que compone la lista 'b'
for elemento in b:
    # vuelve a convertir en str el int del elemento [3] de cada lista ( sublista)
    elemento[3] = str(elemento[3])
    ele = ';'.join(elemento) + '\n'
    completo.write(ele)
print('datosCompletos.csv')
completo.close()