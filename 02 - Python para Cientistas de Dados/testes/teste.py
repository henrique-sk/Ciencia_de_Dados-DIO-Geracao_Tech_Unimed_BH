valores = input().split()

tempo = float(valores[0])
velocidade = float(valores[1])

KM_P_L = 12
litros = (velocidade * tempo) / KM_P_L

print(f'{litros:.3f}')