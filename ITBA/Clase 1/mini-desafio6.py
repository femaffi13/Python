# Mini-desafío: for
# Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado. 
# Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. Luego, para cada producto, 
# se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo. Posteriormente el programa imprimirá 
# dicho código.

# Imprimir en pantalla los códigos solicitados la cantidad requerida de veces.

# Ejemplo:
# Las líneas indicadas con >> corresponden a Inputs. Las líneas sin indicaciones corresponden a Outputs:
# >> 3
# >> 000000123
# >> 1
# 000000123
# >> 123000789
# >> 3
# 123000789
# 123000789
# 123000789
# >> 000031416
# >> 2
# 000031416
# 000031416

cantidadProductos = int(input("Cantidad de productos diferentes que necesitan etiquetas: "))

for producto in range(cantidadProductos):
  codigo = int(input("Ingresar el código a impimir: "))
  cantidad = int(input("Ingresar la cantidad: "))
  for x in range(cantidad):
    print(codigo)