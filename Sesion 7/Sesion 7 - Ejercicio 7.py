def f_mataronistas(datos):

    # sirve para diccionarios
    ordenar_por_nombre=sorted(datos,key=lambda x:x['nombre'])
    # print(datos['maratones']['tiempo']) problema original naratones es una LISTA no una DICCIONARIO
    # ordenar_por_tiempo=sorted(datos,key=lambda x:x['maratones'][0]['tiempo'])
    ordenar_por_tiempo = sorted(datos, key=lambda x: min(m['tiempo'] for m in x['maratones']))
    return ordenar_por_tiempo

maratonistas=[
    {'nombre':'Ajuan','dni':1223,'maratones':[
        {
        'nombre':'nigeria',
        'anio':2023,
        'puesto':4,
        'tiempo':10,
         },
        {
        'nombre':'bs as ',
        'anio':2023,
        'puesto':1,
        'tiempo':6,
        },
        {
        'nombre':'albania',
        'anio':2022,
        'puesto':1,
        'tiempo':7,
        }
    ]
    },

    {'nombre':'carlos','dni':12243,'maratones':[
        {
        'nombre':'albania',
        'anio':2023,
        'puesto':4,
        'tiempo':6.32,
         },
        {
        'nombre':'bs as',
        'anio':2023,
        'puesto':2,
        'tiempo':2,
        },
        {
        'nombre':'asia',
        'anio':2022,
        'puesto':1,
        'tiempo':88,
        }
    ]
    }
]
print(f_mataronistas(maratonistas))