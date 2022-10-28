contatos = {
  "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
print(contatos)
print("=" * 100)

del contatos["henrique@gmail.com"]["telefone"]
print(contatos)
print("=" * 100)

del contatos["chappie@gmail.com"]
print(contatos) # {'henrique@gmail.com': {'nome': 'Henrique'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}