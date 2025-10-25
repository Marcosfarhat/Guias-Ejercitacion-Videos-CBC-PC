# creo el diccionario
estudiantes={}
cursos={}
# Ingreso la clave por primera vez (DNI)
print('Ingrese su DNI o cliquea * para abandonar el ingreso ')
dni=input('DNI: ')
# entro en ciclo inexacto para pedir los valores de la clave DNI
while dni !='*':
    nom=input('nombre : ')
    ape=input('apellido: ')
    edad=int(input('edad '))
    while edad not in range(18,130):
        edad = int(input('edad'))
    # valores del diccionario curso
    # curso=input('curso :')
    # anio=input('anio : ')
    # division=input('division :')
    # orientacion=input('orientacion : ')
    # # guardo los valores en el diccionrio curso
    # cursos[curso]=[anio,division,orientacion]
    # guardo los valores en el diccionario con la clave DNI
    estudiantes[dni]=[nom,ape,edad]
    # Pido datos nuevamenete ahora dentro del ciclo inexacto
    print('Ingrese un nuevo DNI o cliquea * para abandonar el ingreso ')
    dni = input('DNI: ')
# me da la clave del estudiante mas viejo
edad_max=max(estudiantes,key=lambda k:estudiantes[k][2])
print(edad_max)
# tomo el valor de edad ( valos 2 )
edad_maxima = estudiantes[edad_max][2]
print('edad maxima ',edad_maxima)
for per in estudiantes:
    # * me devuelve todos los valores de la clave
    print('1',per,*estudiantes[per])
    print('-------------------------------')
    # me devuelve solo los valores que pido
    print('2',per,estudiantes[per][0],estudiantes[per][1],estudiantes[per][2])




