#Crear lista con nombres
Admitidos = ["Antonio","Richard","Sara","Andrea"]

#Pedir Nombre del usuario
Usuario = str(input("Ingrese su nombre: "))

#Validar que el nombre este en la lista
if Usuario in Admitidos:
    print("Estas en la lista")
else:
    print("No estas en la lista")
