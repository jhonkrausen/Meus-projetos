fibonacci = [0,1]
soma = 0
i = 1
while soma < 1600:
    soma = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(soma)
    i = i + 1

print(soma)