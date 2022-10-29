def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

print("=" * 50)
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

print("=" * 50)
criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido