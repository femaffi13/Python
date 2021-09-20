# Mini-desafío: Operadores
# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, 
# y se muestre a la salida el promedio de los tres números.

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))
promedio = (n1+n2+n3) / 3
print(f"El promedio es: {promedio}")

# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, 
# y se muestre a la salida la media geométrica de los tres números.

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))
mediaGeometrica = (n1*n2*n3)**(1/3)
print(f"La media geométrica es: {mediaGeometrica}")