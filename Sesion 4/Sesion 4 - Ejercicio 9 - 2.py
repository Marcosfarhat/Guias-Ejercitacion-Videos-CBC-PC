libros =['El principito','it','Sherlock Holmes',"it", "el homnbre que rie",'it']
lista_libros = []
for i in libros:
    if i not in lista_libros:
        lista_libros.append(i)
        cuantos_libros_hay = libros.count(i)
        print(cuantos_libros_hay,i)

