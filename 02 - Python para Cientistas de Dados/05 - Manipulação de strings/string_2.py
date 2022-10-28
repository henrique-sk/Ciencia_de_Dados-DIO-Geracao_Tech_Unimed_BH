nome = "Henrique"
idade = 36
rofissao = "Programador"
linguagem = "Python"
saldo = 45.654

dados = {"nome": "Henrique", "idade": 36}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {age} {nome} {nome} {age}".format(nome=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} saldo: {saldo:.2f}')
print(f'Nome: {nome} Idade: {idade} saldo: {saldo:10.1f}')
print(f'{saldo:.2f}')