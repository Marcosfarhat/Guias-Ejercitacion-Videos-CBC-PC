primo_o_no_primo = int(input("ingresa un numero y te digo si es primo o no: "))
primo = 0
for primo in range(2, primo_o_no_primo):
    if primo % 2 == 0 and  primo != 2 or  primo % 3 == 0 and primo != 3 or primo % 5 == 0 and primo !=5 or  primo % 7 == 0 and primo !=7  :
        no_es_primo=1
    else:
         print(f"El numero {primo} es primo ")
    # elif primo % 3 != 0 or primo == 3:
    #     print(f"El numero {primo} es primo")
    #     print("Resto de 3"
    # else print(f"El numero {primo} es primo"):