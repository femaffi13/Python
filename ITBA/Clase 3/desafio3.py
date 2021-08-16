#Realizar un programa en el cual se decida el ganador de unas elecciones.

# El programa primero recibe un número  N , la cantidad de votos totales que se realizaron. 
# Luego recibe  N  votos en formato string, cada uno consiste en el nombre del candidato seleccionado. 
# El programa debe calcular el ganador e imprimir su nombre, para este ejemplo se asume que no hay empates. 
# Los nombres y la cantidad de candidatos es desconocida.

# Ejemplo:
# Input:
# 12
# Mickey
# Donald
# Mickey
# Minnie
# Mickey
# Goofy
# Daisy
# Goofy
# Goofy
# Minnie
# Goofy
# Donald
# Output:

# Goofy
# El resultado es Goofy ya que este recibe 4 votos, la cual es la mayor cantidad de votos.

n = int(input('Cantidad de votos: '))
candidatos = []
for x in range(n):
    voto = input('Candidato: ').capitalize()
    candidatos.append(voto)
ganador = ''
maxVotos = 0
for i in range(len(candidatos)):
    if candidatos.count(candidatos[i]) > maxVotos:
        maxVotos = candidatos.count(candidatos[i])
        ganador = f'{candidatos[i]}'
    
print(ganador)
    