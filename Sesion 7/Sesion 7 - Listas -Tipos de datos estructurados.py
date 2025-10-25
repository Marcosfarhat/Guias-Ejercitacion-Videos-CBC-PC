#prueba de heterogeneidad
a={1:1,2:4,3:6,4:8,5:10}
b={}
c={'ana':27,'juan':15,'elena':1}
wd={345:('clavos',1),346:('tuercas',1),202:('manguera',2)}
h=[1,2,3,4]
i=["juan","pedro","albnerto","santiago"]
# print(d[3],d['ella'][0],d['yo'])
print('popitem= ',a.popitem())
print("diccionario d",wd)
nuevo_diccionario = wd.fromkeys(h," ")
print("nuevo diccionario creado con d.fromkeys()",nuevo_diccionario)
lista_creada_items=a.items()
print("lista creada con ad.items = ",lista_creada_items)
# a.items en ciclo for
for clave, valor in a.items():
    print(clave, valor)

# d.update() agrega o crea un par "clave , valor"
a.update(c)
print(a)