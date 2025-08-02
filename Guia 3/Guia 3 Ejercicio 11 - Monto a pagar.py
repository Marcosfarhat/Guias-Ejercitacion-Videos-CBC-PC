def poniendo_estaba_la_ganza():
    pago = int(input("Ingresa el monto que tenes que pagar"))
    ingreso = 0
    while ingreso < pago:
        ingreso += int(input("Ingrese su deposito"))

poniendo_estaba_la_ganza()
print("Saldo completado")