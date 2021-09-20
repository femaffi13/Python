# Mini-desafío: Funciones
# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan
# Contraseña: 12345_

# Usuario: Pablo
# Contraseña: xDcFvGbHn

# La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.

def verificar(usuario, contraseña):
  if usuario == "Juan":
    if contraseña == "12345_":
      return True 
  elif usuario == "Pablo":
    if contraseña == "xDcFvGbHn":
      return True
    else:
      return False
  else:
    return False 

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
verificar(usuario, contraseña)


# Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.

# Ejemplos:
# contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)
# contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)

def cantDivisores(num):
  contador = 0
  divisor = num  
  for x in range(num):
    if num % divisor == 0:
      contador += 1
    divisor-=1
  return contador

num = int(input("Escribir un número: "))
cantDivisores(num)