from  random import randint
a=[]
for i in range(20):
    a.append(randint(1,35))
print('Segunda Mitad')
for n in a[10:]:
    print(n,end=' ')
print()
print('Primera Mitad')
for n in a[:10]:
    print(n,end=' ')
print()
