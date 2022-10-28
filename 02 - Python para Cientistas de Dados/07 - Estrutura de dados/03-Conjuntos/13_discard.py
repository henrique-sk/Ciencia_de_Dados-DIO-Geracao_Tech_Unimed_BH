numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.discard(1)
print(numeros)

numeros.discard(45)
print(numeros)

numeros  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
print(numeros)