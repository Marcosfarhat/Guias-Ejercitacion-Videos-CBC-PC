carlitos = int(input("Ingrese un numero para dividir-dividendo "))
pedrito = int(input("Ingrese un numero divisor "))
def division(dividendo,divisor):
    if divisor == 0:
        return "error"
    return dividendo / divisor
print(division(carlitos,pedrito))
