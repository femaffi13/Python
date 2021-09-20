# Realizar un programa que decodifique código morse. El usuario debe ingresar una palabra en código morse, 
# usando una secuencia de puntos, guiones y espacios como la siguiente:

# .--. .-. --- --. .-. .- -- .- -.-. .. --- -.

# Luego separando por espacios, cada letra debe ser convertida de morse a una letra del alfabeto,
#  y por último la traducción se muestra en pantalla como un string. Para lo cual, les proponemos definir
#  un diccionario que ayude a realizar la traducción. Es importante considerar qué dato será la clave,
#  y cuál el contenido, de forma en que les sea más útil para lograr el objetivo.

# Tips: Revisar los métodos .split() y .join() para convertir entre strings y listas.

palabra = input('Ingresar palabra en morse: ')

dicc = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

lista = palabra.split(" ")
print(lista)
nueva=[]
for letra in lista:
    if letra in dicc:
        nueva.append(dicc[letra])

morse = ''.join(nueva)
print(morse)