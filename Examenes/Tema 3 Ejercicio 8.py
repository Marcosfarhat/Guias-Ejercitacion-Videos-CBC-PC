def edita(t,carEsp):
    lista=list(t)
    for i in range(len(lista)):
        if lista[i] in carEsp:
             lista[i]='<esp>'
    t=''.join(lista)
    return t.upper()
txt='esta historia continuará   '
print(edita(txt,' '))