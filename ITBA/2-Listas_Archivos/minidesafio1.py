# Mini-desafío: floats
# Crear:
# Una función que convierta grados Celsius a grados Farenheit (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
# Una función que convierta grados Celsius a grados Kelvin (https://es.wikipedia.org/wiki/Kelvin)

# El usuario debe ingresar una temperatura en grados Celsius y el programa debe mostrar las conversiones 
# a Farenheit y Kelvin utilizando las funciones. Si la temperatura ingresada es inferior al cero absoluto, 
# el programa debe mostrar un mensaje de advertencia.

def celsiusFarenheit(celsius):
    return (1.8*celsius) + 32

def celsiusKelvin(celsius):
    return celsius + 273.15

celsius = float(input("Ingresar una temperatura en grados Celsius: "))
if celsius < -273.15:
    print("Temperatura debajo del cero absoluto")
print(f"Temperatura en Farenheit: {celsiusFarenheit(celsius)} ºF")
print(f"Temperatura en Kelvin: {round(celsiusKelvin(celsius),3)} K")