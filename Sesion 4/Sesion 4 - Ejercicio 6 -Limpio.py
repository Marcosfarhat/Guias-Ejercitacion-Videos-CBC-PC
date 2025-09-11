# a
personas = ['juan','ana','paula','alberto','carla']
ultimo=len(personas)
nombre_carla=personas[4]
print(nombre_carla)
personas[ultimo-1]='juan'
print(personas)
print('--------------')
# b
personas = ['juan','ana','paula','alberto','carla']
ultimo=len(personas)
# Recordar que len() cuenta desde 1
personas[ultimo-3]='juan'
print(personas)
# c
print('--------------')
print(personas[0:ultimo])

print('--------------')
personas = ['juan','ana','paula','alberto','carla']
ultimo=len(personas)
for num in range(0,ultimo):
    print(personas[num])

print('--------------')
print(personas*3)