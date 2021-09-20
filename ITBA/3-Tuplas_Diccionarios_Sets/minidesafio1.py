# Realizar un programa que pida al usuario un número de legajo y el nombre completo, 
# luego lo guarde en un diccionario. En caso de que el número de legajo ya se encuentre en el diccionario, 
# se debe mostrar un mensaje de advertencia.

num = int(input('Número de legajo: '))
nombre = input('Nombre completo: ')

dicc = {
    1:'a',
    2:'b'
}

if num in dicc:
    print('Advertencia. El número de legajo ya se encuentra registrado')
else:
    dicc[num] = nombre 
    print(dicc)
