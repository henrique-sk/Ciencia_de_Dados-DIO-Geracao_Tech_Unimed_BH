contatos = {
  "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

teste = "henrique@gmail.com" in contatos # True
print(teste)

teste = "megui@gmail.com" in contatos # False
print(teste)

teste = "idade" in contatos["henrique@gmail.com"] # False
print(teste)

teste = "telefone" in contatos["giovanna@gmail.com"] # True
print(teste)