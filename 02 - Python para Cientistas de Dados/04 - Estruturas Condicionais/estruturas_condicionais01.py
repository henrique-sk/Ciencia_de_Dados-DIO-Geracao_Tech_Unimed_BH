MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
  print("Ainda não pode tirar CNH.")

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar CNH.")
else:
  print("Ainda não pode tirar CNH.")

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
  print("Pode fazer aulas teóricas.")
else:
  print("Ainda não pode tirar CNH.")



# saldo = 2000.0
# opcao = float(input("Informe uma opção: [1] Sacar\n [2] Extrato: "))

# if opcao == 1:
#   print("Realizando saque!")
# else:
#   print("Saldo insuficiente!")
