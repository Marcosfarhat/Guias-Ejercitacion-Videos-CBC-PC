from idlelib.replace import replace

cadena = 'Camppeones del mundo  = 2022'
def elimando(palabra):
    return palabra.replace('2022','')

cadena_eliminada = elimando(cadena)
print(cadena_eliminada)