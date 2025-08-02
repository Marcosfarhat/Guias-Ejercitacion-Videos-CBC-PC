def primo():
    primo_o_no_primo = int(input("Ingresa un número y te digo si es primo o no: "))

    # Check if the number is less than 2
    if primo_o_no_primo < 2:
        print(f"El número {primo_o_no_primo} no es primo.")
        return

    # Assume the number is prime until proven otherwise
    es_primo = True

    for i in range(2, int(primo_o_no_primo ** 0.5) + 1):
        if primo_o_no_primo % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El número {primo_o_no_primo} es primo.")
    else:
        print(f"El número {primo_o_no_primo} no es primo.")


primo()