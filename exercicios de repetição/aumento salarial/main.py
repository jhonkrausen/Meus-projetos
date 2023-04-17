anoInicial = 1996
anoFinal = 2023
aumento = 0.015
salario = float(input("Digite seu salário: "))

for i in range(anoInicial, anoFinal):
    aumento = aumento* 2
    salario = salario * aumento
print(f"Salário atual: R% {salario}")