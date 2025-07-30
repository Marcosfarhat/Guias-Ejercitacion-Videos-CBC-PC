''' '
hay_sol = True
hace_frio = True
if hay_sol and not hace_frio:
    print("Voy en tanga")
elif hay_sol and hace_frio:
    print("Voy con buzo y tanga")
else:
    print("Voy con la jogguineta ")
'''

# Pregunto
hay_sol = 0
hace_frio = 0
hay_sol = bool(int(input("Hay Sol 1-SI  0-NO ")))
hace_frio  = bool(int(input("Hace Frio 1-SI  0-NO ")))
print(hay_sol)
print(hace_frio)
if hay_sol and not hace_frio:
 print ("Voy de cuerpo gentil ")
elif not hay_sol and hace_frio:
 print("Voy abrigado ")
else:
 print("Voy de cualquier manera")
