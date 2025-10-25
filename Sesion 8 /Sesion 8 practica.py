print('Luciana;Jurez;Santiago del Estero;95'.split(';'))

a = ['uno', 'dos', 'tres']
for i in range(len(a)):
     print(a[i])

with open('datosCompletos.csv','r') as archico:
     lines=archico.readlines()
     print(lines)

# Resultado: ['Luciana', 'Jurez', 'Santiago del Estero', '95']