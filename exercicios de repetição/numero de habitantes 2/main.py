paisA = float(input("Digite a população do pais A: "))
crescimentoA = float(input("Digite a taxa de crescimento do país A(sem %): "))
paisB = float(input("Digite a população do pais B: "))
crescimentoB = float(input("Digite a taxa de crescimento do país B(sem %): "))
anos = 0
crescimentoA = crescimentoA / 100
crescimentoB = crescimentoB / 100
while paisA < paisB:
    paisA = paisA + (paisA * crescimentoA)
    paisB = paisB + (paisB * crescimentoB)
    anos = anos + 1

print(f"Serão necessários {anos} anos para que o pais A ultrapasse ou iguale a população do pais B")