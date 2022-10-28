#Conjuntos (SETs) não suportam indexção, para exibir tem de ser transformados em lista
numeros = {1, 2, 3, 2}
# print(numeros[0]) #dá erro

numeros = list(numeros)

print(numeros[0])