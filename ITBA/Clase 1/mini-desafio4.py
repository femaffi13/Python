# Mini-desafío: if
# Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) utilizando un if/else.
# La nota será ingresada por el usuario usando input().

nota = int(input("Nota: "))
if nota >= 4 and nota <= 10:
  print("Aprobado!")
elif nota >= 0 and nota < 4:
  print("Desaprobado..")
else: 
  print("Nota fuera de rango (0-10)")

# Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de 
# acuerdo a la siguiente conversión:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: 0–59

nota = int(input("Nota (0-100): "))
if nota > 0 and nota < 60:
  print("F")
elif nota >= 60 and nota < 70:
  print("D")
elif nota >= 70 and nota < 80:
  print("C")
elif nota >= 80 and nota < 90:
  print("B")
elif nota >= 90 and nota < 100:
  print("A")
else:
  print("Nota fuera de rango (0-100)")
