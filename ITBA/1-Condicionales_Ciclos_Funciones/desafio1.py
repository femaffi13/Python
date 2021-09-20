# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
# Si el número es par, se debe dividir por  2.
# Si el número es impar, se debe multiplicar por 3 y sumar 1.
# Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

# Ejemplos:
# Input: 6
# Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)

# Input: 13
# Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)

print("Conjetura del Dr. Lothar".center(60, '-'))
num = int(input("Ingrese un número: "))
pasos = 0
while num != 1:
    if num % 2 == 0:
        num = num / 2
    elif num % 2 != 0:
        num = (num * 3) + 1
    pasos += 1
print(f"Cantidad de pasos que tardó en llegar: {pasos}")

