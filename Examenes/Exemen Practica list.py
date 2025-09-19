lista=[ 'el','como']
nueva_lista= []
for i in lista:
    for v in i:
        nueva_lista.append(list(v))
        print(nueva_lista)