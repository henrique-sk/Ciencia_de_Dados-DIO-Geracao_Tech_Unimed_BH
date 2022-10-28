contatos = {
"henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"}
}

copia = contatos.copy()
print(copia)

copia["henrique@gmail.com"] = {"nome": "Hank"}
print(copia)

print(contatos["henrique@gmail.com"]) # {"nome": "Henrique", "telefone": "3333-2221"}

print(copia["henrique@gmail.com"]) # {"nome": "Hank"}