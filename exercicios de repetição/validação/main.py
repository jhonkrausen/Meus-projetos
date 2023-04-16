
nome = str(input("Digite seu nome: "))
while len(nome) < 3:
    nome = str(input("O nome deve ter mais de 3 caracteres! digite novamente: "))

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("A idade deve estar entre 0 e 150 anos! digite novamente: "))

salario = float(input("Digite seu salário: "))
while salario < 0:
    print("Seu salário deve ser maior que 0! digite novamente: ")

sexo = str(input("Digite seu sexo M/F: "))
while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
    sexo = str(input("Você deve digitar 'M' ou 'F'! digite novamente: "))

estadoCivil = str(input("Digite seu estado civil:\n'S' para solteiro(a)\n'C' para casado(a)\n'D' para divorciado(a)\n'V' para viúvo(a)"))
while estadoCivil != "c" and estadoCivil != "s" and estadoCivil != "d" and estadoCivil != "V" and estadoCivil != "C" and estadoCivil != "S" and estadoCivil != "D" and estadoCivil != "v":
    estadoCivil = str(input("Você deve digitar 'S', 'C', 'D' ou 'V'! digite novamente!"))
