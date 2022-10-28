def exibir_poema(data_extenso, *args, **kwargs):
# ef exibir_poema(data_extenso, *lista, **dicionario): # args e kwargs podem ter o nome que quiser
  texto = "\n".join(args)
  meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
  mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
  print(mensagem)

exibir_poema(
  "Sexta-feira, 28 de Outubro de 2022",
  "Zen of Python",
  "Beautiful is better than ugly.",
  autor="Tim Peters", ano=1999)

print("=" * 100)

exibir_poema(
  "Sexta-feira, 28 de Outubro de 2022",
  *("Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex."),
  **{"autor": "Tim Peters", "ano": 1999})

print("=" * 100)

exibir_poema(
  "Sexta-feira, 28 de Outubro de 2022",
  "Zen of Python",
  "Beautiful is better than ugly.",
  "Explicit is better than implicit.",
  "Simple is better than complex.",
  autor="Tim Peters",
  ano=1999)