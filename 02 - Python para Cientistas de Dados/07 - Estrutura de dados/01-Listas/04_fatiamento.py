lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # ["t", "h", "o", "n"]
print(lista[:2]) # ["p", "y"]
print(lista[1:3]) # ["y", "t"]
print(lista[0:3:2]) # ["p", "t"] aqui, 3 é o ponto de parada e 2 é o step (de 2 em 2)
print(lista[::]) # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1]) # ["n", "o", "h", "t", "y", "p"]