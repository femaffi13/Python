# Mini-desafío: Operaciones sobre una lista
# Realizar un programa que ordena nombres alfabéticamente. Primero debe pedir al usuario que ingrese un número: 
# la cantidad de nombres que serán ingresados. Luego debe pedir al usuario que ingrese un nombre
#  y repetir ese pedido la cantidad de veces indicada. Los nombres se deben ir agregando a una lista.
#  Por último, ordenar la lista alfabéticamente y mostrar en pantalla de a uno por vez los nombres ordenados 
# (usando un for).

cantidad = int(input("Cantidad de nombres a ingresar: "))
lista = []
for x in range(cantidad):
    nombre = input("Ingresar un nombre: ")
    lista.append(nombre)
lista.sort()
print("Nombres ordenados alfabéticamente".center(50, '-'))
for nombre in lista:
    print(nombre)