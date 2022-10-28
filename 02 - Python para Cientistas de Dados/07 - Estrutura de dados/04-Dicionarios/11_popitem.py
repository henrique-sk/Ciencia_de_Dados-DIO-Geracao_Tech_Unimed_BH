# sem informar a chave, vai retirando os itens na sequencia
contatos = {
"henrique@gmail.com": {"nome": "Henrique","telefone": "3333-2221"}
}
print(contatos)

contatos.popitem() # ('henrique@gmail.com', {'nome': 'Henrique', 'telefone': '3333-2221'})
print(contatos)

# contatos.popitem() # KeyError