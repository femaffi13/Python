# Mini-desafío: Listas
# Crear una lista con los números pares menores a 50 ¿Hay diferentes formas de lograr esto?

pares = [2*x for x in range(25)]
print(pares)
pares2 = [x for x in range(0,50,2)]
print(pares2)

# Crear un programa en el cual el usuario ingresa un string y dos índices numéricos. 
# El programa debe crear una lista a partir de las letras del string, luego intercambiar dos letras de lugar 
# a partir de los índices indicados por el usuario. Por último debe combinar las letras de la lista nuevamente 
# en un string e imprimir el resultado. Si los índices son inválidos mostrar un mensaje de error.

# Tips:
# Usando list( mi_string ) pueden obtener una lista que contiene las letras de mi_string.
# Usando el método str.join() pueden unir las letras o strings de una lista dentro de un mismo string:
# lista = ["Uno", "Dos", "Tres"]
# texto = "".join( lista )
# A la izquierda del .join() se indica el string con el cual unir los elementos como por ejemplo ", ".
#  Si utilizamos un string vacío no intercala ningún caracter entre los elementos.

cadena = input("Ingresa una cadena de texto: ")
indice1 = int(input("Primer índice: "))
indice2 = int(input("Segundo índice: "))
if indice1 >= len(cadena) or indice2 >= len(cadena):
    print("Error, sobrepasa los índices")

lista = list(cadena) #Casteo la cadena a lista
letra = lista[indice1] #Guardo la primer letra a intercambiar
lista[indice1] = lista[indice2]
lista[indice2] = letra 
texto = "".join(lista) #Lista a cadena 
print(texto)