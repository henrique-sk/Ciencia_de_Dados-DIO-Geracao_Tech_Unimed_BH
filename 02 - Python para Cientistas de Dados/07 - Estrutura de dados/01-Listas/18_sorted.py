linguagens = ["python", "js", "c", "java", "csharp"]

# sorted não modifica a ordem da lista (é só para "mostrar" naquele momento)
print(sorted(linguagens, key=lambda x: len(x))) # ["c", "js", "java", "python", "csharp"]

print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ["python", "csharp", "java", "js", "c"]

print(sorted(linguagens))