contato = {'nome': 'Henrique', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna") # "Henrique"
print(contato) # {'nome': 'Henrique', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # 28
print(contato) # {'nome': 'Henrique', 'telefone': '3333-2221', 'idade': 28}