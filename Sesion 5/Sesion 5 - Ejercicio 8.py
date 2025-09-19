tupla = ('juan', 'pedro', 'alberto')
sacar = input('Quien no viene?')

def sacar_invitado(invitado):
    if invitado  == sacar:
         return False
    else:
        return True

lista_nueva = list(filter(sacar_invitado,tupla))
print(lista_nueva)