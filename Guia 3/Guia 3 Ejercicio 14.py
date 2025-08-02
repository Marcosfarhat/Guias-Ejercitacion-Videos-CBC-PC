def primo():
    primo_o_no_primo = int(input("ingresa un numero y te digo si es primo o no: "))
    primo = 0
    for primo in range(2,primo_o_no_primo):
        if primo %2 != 0 or primo==2:
            if primo %3 !=0 or primo ==3:

                if primo %5 !=0 or  primo ==5:
                    if primo %7 !=0 or  primo ==7:
                        print(f"El numero {primo} es primo")
primo()
"""
  or  
 primo_o_no_primo = int(input("ingresa un numero y te digo si es primo o no: "))
primo = 0

for primo in range(2, primo_o_no_primo):
    if primo % 2 == 0 and  primo != 2 or  primo % 3 == 0 and primo != 3 or primo % 5 == 0 and primo !=5 or  primo % 7 == 0 and primo !=7  :
        no_es_primo=1
    else:
        print(f"El numero {primo} es primo ")
"""