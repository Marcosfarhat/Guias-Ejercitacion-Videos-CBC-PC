argentina= ('argentina',' buenos aires','america')
francia = ('francia','paris','europa')
alemania= ('alemania','berlin','europa')
japon =  ('japon','tokio','asia')
peru = ('peru','lima','america')
'''-----------B-------------'''
lista = [argentina,francia,alemania,japon,peru]
print(lista)
'''-----------C-------------'''
''' hacer una funacion que recima por parametros la lista , eimprima la infomacion de cada pais en el formato dado'''
def paises(a):
   for n in a:
       print('Pais:', n[0])
       print('Capital:', n[1])
       print('Continente:',n[2])
       print('----------------------')

paises(lista)
'''-----------D-------------'''
''' Hacer una funcion que haga lo mismo que hice en B, o sea agregar las tuplas a la lista'''
def tuplas_a_la_lista():

