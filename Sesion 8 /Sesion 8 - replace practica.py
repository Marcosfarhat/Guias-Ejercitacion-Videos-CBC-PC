tupla=('carla','veronica', 'myriam')
reemplazo=[]
# i es un str de tupla o sea que en el FOR  tupla devuelve un STR 'i'
for i in tupla:

    print(i)
    # agrego.append(i)
    # .append funciona sobre listas y replace sobre str
    reemplazo.append(i.replace('carla','luna'))


print(reemplazo)

