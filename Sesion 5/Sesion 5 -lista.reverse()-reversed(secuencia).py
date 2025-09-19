lista = [ 1,2,3,4,]
tupla = (1,2,3,4)
tupla_2 = ('a','b','c')
'''lista.reverse()
print(list(reversed(tupla)))
tupla = tuple(tupla)
print(lista)
print(tupla)'''''

tupla_reversa = tuple(reversed(lista))
print(tupla_reversa)

devuelta_tupla_2 = reversed(tupla_2)
txt = list(devuelta_tupla_2)
print(type(devuelta_tupla_2))
print(txt)
txt_sin_comas = ''.join(txt)
print(f'texto invertido sin comas {txt_sin_comas}')
'''
juntos =[]
print('con ciclo for para la secuencia ')
print('----------------------')
for i in devuelta_tupla_2:
    juntos.append(i)
    txt = ''.join(juntos)
    print(juntos)
    print(txt)'''