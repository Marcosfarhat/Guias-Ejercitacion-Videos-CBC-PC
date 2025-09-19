def edita(t,letra):
    lista=t.split()
    for pal in lista:
        if pal in letra:
            pos=letra.index(pal)
            print(pos)
            pal=str(pos)
    t=' '.join(lista)
    return letra


txt='Media docena es seis , el par son dos'
letra=['cero','un','dos','tres','cuatro','cinco','seis']

print(edita(txt,letra))