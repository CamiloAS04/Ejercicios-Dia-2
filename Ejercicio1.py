#Pedir tres numeros al usuario
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))
numero3 = int(input("Ingresa tercer numero: "))

#Comparar con condicionales
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

#Mostrar resultado
print("el numero mas pequeño es:", menor)