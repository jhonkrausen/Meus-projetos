paisA = 80000
paisB = 200000
anos = 0
while paisA < paisB:
    paisA = paisA * 1.03
    paisB = paisB * 1.015
    anos = anos + 1

print(f"Serão necessários {anos} anos para que o pais A ultrapasse ou iguale a população do pais B")