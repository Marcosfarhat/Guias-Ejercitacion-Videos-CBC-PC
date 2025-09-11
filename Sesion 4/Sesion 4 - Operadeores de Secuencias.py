'''print('----------------')
print('x in s')
s = [1,2,3,4]
for x in s:
    if x ==3:
        print("Hola, soy el 3")
    else:
        print("no se que pasa")
print('----------------')
print('s+d')
d = [5,6,7,8]
print(s+d)
print('----------------')
print('s*d')
print(s*5)
print('----------------')
i=s[2]
print(s[1])
print('----------------')
print(s[-2])'''
from itertools import count
'''
s = [1,2,3,4,5,6,7,8]
 print('----------------')
print(s[2:5])
print('----------------')
print(s[1:6:2])
print('----------------')
a = ["hola",'como','estas',3,4,7]
print(a[1:4])
print('----------------')
b=[1,4,56,76]
print(max(b))
print('----------------')
print(sorted(b))
print('----------------')
c=['avs','bad','cdd','edo','ingle','mastodonte','onirico', 'pusilanime']
print(sorted(c))
'print('----------------')
print("invertido")
print( list(reversed(c)))
print('----------------')
# contar palabra dentro  secuencia dentro
print(len(c[7]))
print('----------------')
d="hola"
print(len(d))
print('----------------')
a="a","b","z","o"
print(sorted(a))
'''

print('----------------')
print('count')
e=1,1,1,1,2,3,4,4,4,5,5,6,7
print(e.count(1))
print(e.count(4))
print('----------------')
print('index')
e=1,1,1,1,2,3,4,4,4,5,5,6,7
print(e.index(3,1,7))
print('----------------')
print('index simple')
print(e.index(5))
print('----------------')
print('sum')
f=2,2
suma = sum(f)
print(suma)
print('----------------')
print('insert')
f=[2,2,4,5,6]
print(f.insert(1,5))
print(f)





