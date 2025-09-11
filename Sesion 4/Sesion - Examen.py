for i in range(4):
    for j in range(1,2,2):
         print("*")

print('----------------')
i=3
a = i**2
print(a)
print('----------------')
a=[10,20,30]
print(len(a))

print('----------------')
b=['hola','chau','como']
print(len(b))

def mismaVocal(pal):
    cant=0
for letra in 'aeiou':
    if pal.count(letra)>0:
    cant+=1
return cant==1
