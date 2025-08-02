def primo():
    primo_o_no_primo = int(input("ingresa un numero y te digo si es primo o no: "))
    primo = 0
    for primo in range(2, primo_o_no_primo):
        if primo %2 != 0 or  primo ==2 :
            print(f"El numero {primo} es primo")
            print("Resto de 2")

        elif primo %3 !=0 or primo ==3:
               print(f"El numero {primo} es primo")
               print("Resto de 3")
primo()