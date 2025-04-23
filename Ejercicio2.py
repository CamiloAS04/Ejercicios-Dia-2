#Crear una lista con 5 numeros
Numeros = [10,20,30,40,50]

#Pedir numero al usuario
Usurio = int(input("Ingresa numero para verificar que es correcto: "))

#Verificar si el numero esta en la lista
if Usurio in Numeros:
    print("¡El numero esta en la lista!")
else:
    print("El numero NO esta en la lista")