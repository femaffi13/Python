#Mini-desafío: Sets
#1. Se cuentan con varios sets que contienen las personas que les gusta un cierto sabor de helado:

vainilla = { "Juan", "Marina", "Tomas", "Paula" }
chocolate = { "Pedro", "Paula", "Marina" }
dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

# Responder usando operaciones de sets:

# ¿Hay alguna persona que le gusten todos los gustos?
print(vainilla & chocolate & dulceDeLeche)
# ¿Hay alguna persona que le gusten la vainilla y no el dulce de leche?
print(vainilla - dulceDeLeche)
# ¿Cuántas personas distintas tenemos?
print(vainilla | chocolate | dulceDeLeche)

#Diseñar un programa que analiza si una frase es un pangrama del idioma inglés, es decir, 
# que contiene todas las letras del alfabeto al menos 1 vez. El programa debe ser capaz de ignorar 
# espacios y signos de puntuación. Por ejemplo:
frase = "the quick brown fox jumps over the lazy dog"
#El siguiente set puede serles de utilidad:
letras = set("abcdefghijklmnopqrstuwxyz")

# l = []
# for letra in frase:
#     if letra in letras: 
#         l.append(letra)
# print(l)

for x in frase:
    if x in letras:
        letras.remove(x)

if letras == set():
    print('Es pangrama')
else:
    print('No es pangrama')

