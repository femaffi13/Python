# Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y otro jugador 
# intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree que se encuentra 
# en la palabra elegida.

# Una vez que el segundo jugador adivina todas las letras que se encuentran en la palabra, 
# el juego termina y se muestra la cantidad de intentos que fueron necesarios. En esta versión del juego, 
# si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias cuentan como adivinadas.

# Formato del input:
# Primero se recibe la palabra que se debe adivinar (por defecto vendrá en mayúsculas)
# Luego se reciben cierta cantidad de letras, una por línea, sin repetir. (por defecto vendrán en mayúsculas)
# Una vez que se haya adivinado la palabra del ahorcado, ya no se recibirán más letras. Su tarea es determinar 
# la cantidad de intentos que fueron necesarios para adivinar la palabra completa, e imprimir ese número.

palabra = input("Palabra a adivinar: ").upper()
contador = 0

while palabra != "":
    letra = input("Ingresar una letra: ").upper()

    if len(letra) == 1: 
        if letra in palabra: 
            print("La letra está dentro de la palabra.")
            palabra = palabra.replace(letra, "")            
        else:
            print("No está en la palabra.")
    else: 
        print("Ingresar sólo una letra")
                         
    contador += 1

print(f"Ganaste! Número de intentos: {contador}")


# palabra = input("")
# contador = 0

# while palabra != "":
#     letra = input("")   

#     if len(letra) == 1: 
#         if letra in palabra:             
#             palabra = palabra.replace(letra, "")                                      
#     contador += 1
# print(f"{contador}")
