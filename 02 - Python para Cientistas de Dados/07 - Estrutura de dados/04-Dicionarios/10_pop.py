contatos = {
"henrique@gmail.com": {"nome": "Henrique","telefone": "3333-2221"}
}
print(contatos)

result = contatos.pop("henrique@gmail.com") # {'nome': 'Henrique', 'telefone': '3333-2221'}
print(result)

result = contatos.pop("henrique@gmail.com", {}) # {}
print(result)