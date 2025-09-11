'''print('hola'.capitalize())
print('------------------')
print('hola'.center(11,'*'))
print('------------------')
print('python'.find('th'))
print('------------------')
print('python programming'.rfind('th'))
print('------------------')
print('Mi nombre es {}y tengo {} a\u00f1os'.format('juan','23'))
print('------------------')
nombre = 'Pedro'
edad = 65
print(f'Mi nombre es {nombre} y tengo {edad} a\u00f1os') '''
from idlelib.replace import replace

# print('    hola tierra'.strip())
palabras = 'naranja'
print(palabras.strip('an'))
print('------------------')
url = "www.ejemplo.com//"
print("        www.ejemplo.com//".strip("w/"))  # Output: "ejemplo.com"
print("www.ejemplo.com//".strip("w/"))  # Output: "ejemplo.com"
print('------------------')
print("Hola Hola Hola, como estas".replace("Hola","hi"))
print("Hello, World!".replace("Hello","Hi"))
print("hola hola ola la hola esta de fiesta ".replace("hola","chau"))
print('------------------')
print('auto,caballo,lavarropa'.split(','))
