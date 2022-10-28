contatos = {
"henrique@gmail.com": {"nome": "Henrique","telefone": "3333-2221"}
}
print(contatos)

contatos.update({"henrique@gmail.com": {"nome": "Hank"}})
print(contatos) # {'henrique@gmail.com': {'nome': 'Hank'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos) # {'henrique@gmail.com': {'nome': 'Hank'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}