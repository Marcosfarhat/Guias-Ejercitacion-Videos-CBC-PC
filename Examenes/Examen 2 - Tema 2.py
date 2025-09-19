def sinLetras(t,let):
    lista=list(t)
    for car in let:
        
        lista.remove(car)
    t=''.join(lista)
    return t
txt='esta historia continuara...'
print(sinLetras(txt,'aeiou'))
