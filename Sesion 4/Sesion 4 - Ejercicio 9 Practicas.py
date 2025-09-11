libros =['El principito','it','Sherlock Holmes',"it", "el homnbre que rie",'it']
lista_unica_de_libros =[]
for i in libros:
    if i not in lista_unica_de_libros:
        lista_unica_de_libros.append(i)
        cuenta = libros.count(i)
        print(cuenta,i)


# print(libros)
