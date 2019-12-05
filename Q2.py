total_empregados = 3
valor_desconto = 0.11

matriculas = []
salarios_brutos = []

for i in range(total_empregados):
    matricula = input('\nMatriculas: ')
    salario_bruto = float(input('Salario Bruto: '))
    matriculas.append(matricula)
    salarios_brutos.append(salario_bruto)

print('\nResultado:')


for i in range(total_empregados):
    salario_liquido = salarios_brutos[i] - (salarios_brutos[i] * valor_desconto)
    desconto = salarios_brutos[i] * valor_desconto
    print('\nMatricula: {}'.format(matriculas[i]))
    print('Salario Bruto: R${:.2f}'.format(salarios_brutos[i]))
    print('Desconto: R${:.2f}'.format(desconto))
    print('Salario Liquido: R${:.2f}'.format(salario_liquido))
