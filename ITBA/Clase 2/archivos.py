palabras = []

contador1 = 0
contador2 = 0

for x in range(len(palabras)):
  if palabras[x] == "QUE":
    contador1 += 1
for x in range(len(palabras)):
  if palabras[x] == "CRÁTER":
    contador2 += 1

print(contador1)  
print(contador2)  