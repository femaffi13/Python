# Mini-desafío: while
# Implementar un programa que reciba 2 números (A y B), y luego imprima en pantalla la secuencia de números enteros
# desde A hasta B. En el caso de que B sea menor que A, se debe repetir el pedido de B hasta que sea válido ( B  ≥  A ).

a = int(input("Número A: "))
b = int(input("Número B: "))

while b < a:
  print("B debe ser mayor que A. Ingrese nuevamente:")
  a = int(input("Número A: "))
  b = int(input("Número B: "))

while a <= b:
  print(a)
  a+=1

# Implementar un programa que muestre la siguiente secuencia:
# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0

# Para un desafío mayor: Utilizar 1 solo while, 1 solo if y 1 solo else.
# Es recomendable que la variable usada para contar los pasos se mantenga contando siempre de la misma forma.

i = 1
while i < 11:
  if i < 5:
    print(i)
  else:
    print(10-i)
  i+=1