# Esse programa recebe do usuário o registro de 5 alunos com suas notas e retorna todos os registros

Alunos = [] # Lista vazia

# Registrando as informações
while len(Alunos) < 10:
    nome = (input("Digite o nome do aluno: "))
    Alunos.append(nome)
    nota = float(input("Digite a sua nota: "))
    Alunos.append(f"Nota do aluno = {nota}")

# Retornando as informações
print("\n----------REGISTRO DOS ALUNOS----------\n")
for Aluno in Alunos:
    print(Aluno)

print("\nFim do código...")