estaciones = {
    1: ['enero', 'verano'],
    2: ['febrero', 'verano'],
    3: ['marzo', 'verano-otoño'],
    4: ['abril', 'otoño'],
    5: ['mayo', 'otoño'],
    6: ['junio', 'otoño-invierno']
}

primSemes=[0,10000,25000,67500,48000,33000,29000]
print('Ventas Colección Sweaters Invierno 2025')
for i in range(1,len(primSemes)):
    print(estaciones[i][0],'$',primSemes[i],
          estaciones[i][1].upper())