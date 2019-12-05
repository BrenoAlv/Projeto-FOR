alunos = []

for i in range(50):
    nome = input('\nEntre com o nome: ')
    altura = float(input('Entre com a altura: '))

    aluno = (nome, altura)
    alunos.append(aluno)

print('\n\nAlunos com altura acima de 1.70:')

for aluno in alunos:
    nome = aluno[0]
    altura = aluno[1]

    if altura > 1.7:
        print('\nNome:', nome)
        print('Altura:', altura)