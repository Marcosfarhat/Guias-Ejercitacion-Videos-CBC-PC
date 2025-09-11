''' format'''
print('------------------')
texto = 'HOla mi nombre es {}'
print(texto.format('juan'))
print('------------------')
texo ='bruto: ${bruto} + IVA {iva} =  Neto: $ {neto}'
print(texo.format(bruto = 100, iva = 21+10 , neto=121))
print('------------------')
''' tuplas join'''
tup = ('a','b','c')
print(' chiguagua '.join(tup))
print('------------------')
vocales="aeiou"
numeros="12345"
texto="murcielagos"
print(texto.maketrans(vocales,numeros))