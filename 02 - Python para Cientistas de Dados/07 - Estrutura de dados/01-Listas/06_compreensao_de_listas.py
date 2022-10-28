numeros = [1, 30, 21, 2, 9, 65, 34]

pares_v1 = []
for numero in numeros:
  if numero % 2 == 0:
    pares_v1.append(numero)
print(pares_v1)

pares_v2 = [numero for numero in numeros if numero % 2 == 0]
print(pares_v2)

quadrado_v1 = []
for numero in numeros:
  quadrado_v1.append(numero ** 2)
print(quadrado_v1)

quadrado_v2 = []
quadrado_v2 = [numero ** 2 for numero in numeros]
print(quadrado_v2)