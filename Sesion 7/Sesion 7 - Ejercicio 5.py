nota=[
    {'Nombre':'Juan','Apellido':'Saravia','Intentos':1,'Nota':10},
    {'Nombre':'Pedro','Apellido':'Lorezo','Intentos':2,'Nota':9},
    {'Nombre':'Smith','Apellido':'Garcia','Intentos':1,'Nota':8}
]

def promedio_parcial_1(prom):
     contador=0
     notas_acum=0
     promedio=0
     for dic in prom:
         for clave in dic:
             # print(clave)
             if clave=='Intentos':
                 primer_intento= dic['Intentos']
                 if primer_intento==1:
                     notas_acum+=dic['Nota']
                     contador+=1
                     # print(contador,notas_acum)
     promedio=notas_acum/contador
     print(notas_acum,contador)
     print(promedio)

promedio_parcial_1(nota)