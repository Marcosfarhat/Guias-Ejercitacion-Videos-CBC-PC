from fileinput import close

datos1=open('datos1.csv', encoding='latin-1')
a=datos1.readlines()
print('a antes ', a)
for i in range(len(a)):
    # a[i] = a[i].strip('\n')
    a[i] = a[i].split(';')
    a[i][3] = int(a[i][3])

print('a despues ', a)
datos1.close()