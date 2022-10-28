from cgitb import text


nome = "Henrique"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))

for letra in menu:
  print(letra, end="-")
print()
# "same" as...
print("-".join(menu))