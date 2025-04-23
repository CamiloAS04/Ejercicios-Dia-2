#Pida edad al usuario
Edad = int(input("Ingrese su edad: "))

#Validar si la edad esta en el rango
if Edad < 0 or Edad > 120:
    print ("Edad no valida")
else:
    print ("Edad valida")