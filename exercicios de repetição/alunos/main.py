alunos = int(input("Total de alunos da turma: "))
idades = []

for i in range(1, alunos+1):
    idades.append(int(input(f"Digite a idade do aluno {i}: ")))

soma = sum(idades)
media = soma/len(idades)

if media >=0 and media <= 25:
    print("Esta é uma turma jovem")
elif media >=26 and media <=60:
    print("Esta é uma turma adulta")
elif media > 60:
    print("Esta é uma turma idosa")
