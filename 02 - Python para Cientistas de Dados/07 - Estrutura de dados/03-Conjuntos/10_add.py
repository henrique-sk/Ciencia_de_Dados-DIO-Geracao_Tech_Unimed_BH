sorteio = {1, 23}

# Adiciona somente elementos que não existem no conjunto
sorteio.add(25)  # {1, 23, 25}
sorteio.add(42)  # {1, 23, 25, 42}
sorteio.add(25)  # {1, 23, 25, 42}

print(sorteio)