def fun(t):
    vocales='AEIOUÁÉÍÓÚÜ'
    t=t.upper()
    print(t)
    # cont=0
    # for letra in t:
    #     if letra in vocales:
    #         cont+=1
    # if cont>6:
    #     resp=False
    # else:
    #     resp=True
    # return resp
txt='Una oruga NEGRA en un PAJAR'
print(type(txt))
print(fun(txt))