salario = int(input())
mult = 0

if (0 <= salario <= 600):
    mult = 0.17
elif (600.1 <= salario <= 900):
    mult = 0.13
elif (900.01 <= salario <= 1500):
    mult = 0.12
elif (1500.01 <= salario <= 2000):
    mult = 0.10
else:
    mult = 0.05

reajuste = salario * mult

print(f'Novo salario: {(salario + reajuste):.2f}\n' \
    f'Reajuste ganho: {reajuste:.2f}\n\n' \
    f'Em percentual: {(mult * 100):.0f} %')