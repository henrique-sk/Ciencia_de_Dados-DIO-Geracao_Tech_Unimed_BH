salario = 2000


def salario_bonus(bonus, lista):
  # utilizar global não é uma boa prática
  global salario
  lista.append(2)

  lista_aux = lista.copy()
  lista_aux.append(3)
  print(f"lista aux = {lista_aux}")

  salario += bonus
  return salario

lista = [1] # por ser um objeto imutável, pode ser referenciada sem o global
salario_com_bonus = salario_bonus(500, lista) # 2500
print(salario_com_bonus)
print(lista)