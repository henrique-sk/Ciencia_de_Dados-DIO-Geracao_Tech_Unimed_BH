contatos = {
"henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"}
}

#contatos["chave"] # KeyError pq a chave não existe nesse dict

result = contatos.get("chave") # None (verifica se existe a chave)
print(result)

result2 = contatos.get("chave", {"teste"}) # {} (se informar um segundo argumento, ele insere esse valor como padrão)
print(result)

infos = contatos.get("henrique@gmail.com", {}) # {"henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"}
print(infos)