alunos = []
cont=1
acumulado=0
while cont <=10:
    nome = input('\nNome do Aluno: ')
    nota = float(input('Nota: '))
    acumulado=acumulado+nota
    cont = cont + 1
    aluno = (nome, nota)
    alunos.append(aluno)
media=acumulado/10
print ('Média é {:.2f}'.format(media))
print('\n\nAlunos com nota acima da média:')

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[1]

    if nota >= media:
        print('\nNome:', nome)
        print('Nota:', nota)