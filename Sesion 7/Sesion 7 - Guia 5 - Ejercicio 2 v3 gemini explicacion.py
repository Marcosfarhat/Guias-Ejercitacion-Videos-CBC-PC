plantas = []


def planta_nueva():
    # El prompt para la entrada de datos debe ser claro desde el principio
    ingreso = input('¿Deseas ingresar una planta? (1=sí, 2=no): ')

    # Bucle principal para ingresar plantas
    while ingreso != '2':
        # Validación de la entrada principal
        if ingreso == '1':
            # 1. Error de tipo: input() siempre devuelve una cadena (string).
            # Para la luz, si se espera un booleano, se debe convertir la entrada '1'/'0'
            # o 'si'/'no' a True/False. Usaremos '1' para True y '0' para False.

            especie = input('Ingrese el nombre de la planta: ')

            # Bucle para asegurar que el input de luz sea '1' o '0'
            while True:
                luz_str = input('¿Necesita luz? (1=sí/0=no): ')
                if luz_str in ('1', '0'):
                    # Conversión a booleano: '1' se convierte a True, '0' a False
                    luz = (luz_str == '1')
                    break
                else:
                    print("Entrada no válida. Por favor, ingresa '1' o '0'.")

            # Bucle para asegurar que el input de precio sea un número válido
            while True:
                try:
                    precio = float(input('Ingrese el precio: '))
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número para el precio.")

            # 2. Error de estructura de datos: Se usó un set ({}) en lugar de un diccionario ({:})
            # Un set NO mantiene el orden y NO permite acceder a los datos por nombre (clave).
            # Se usa un diccionario para almacenar datos con nombre (clave:valor).
            planta = {
                'especie': especie,
                'luz': luz,
                'precio': precio
            }

            print(f"Planta agregada: {planta}")
            plantas.append(planta)

        else:
            # Manejo de entrada no válida ('1' o '2')
            print("Opción no válida.")

        # Pedir la siguiente acción (al final del if/else y dentro del while)
        ingreso = input('¿Deseas ingresar otra planta? (1=sí, 2=no): ')

    # 3. Error de ordenamiento: NO se puede usar .sort() en una lista de diccionarios
    # sin especificar una 'key' de ordenamiento, ya que Python no sabe cómo compararlos.
    # El código original hacía plantas.sort() dentro de la función y comentaba sorted(plantas) fuera.
    # Si se quisiera ordenar, sería así (por ejemplo, por 'precio'):
    # plantas.sort(key=lambda p: p['precio'])

    return plantas


planta_nueva()
print("\nLista final de plantas:")
print(plantas)