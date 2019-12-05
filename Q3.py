from time import sleep
pessoa = list()
cont = 1
while cont <= 100:
    print("Bem vindo, vamos cadastrar algumas pessoas!")
    print("O código será auto incrementado!")
    nome = str(input("Nome: "))
    telefone = int(input("Telefone: "))
    cont +=1
    pessoa.append([nome,telefone])
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in 'Nn':
        break
print('=' * 30)
print(f'{"Código":<10}{"Nome":<10}{"Telefone":<8}')
print('-' * 30)
for i, a in enumerate(pessoa):
    print(f'{i:<4}{a[0]:>10}{a[1]:>10}')
while True:
    print('-' * 30)
    opc = int(input("Digite o código para fazer uma pesquisa (999 interrompe): "))
    if opc == 999:
        print('FINALIZANDO...')
        print('Volte Sempre!')
        break
    if opc <= len(pessoa)-1:
        print("Checando banco de dados. Por favor, espere...")
        print(1)
        sleep(2)
        print(2)
        sleep(2)
        print(3)
        sleep(2)
        print(f'Os dados encontrados desta pessoa foram: {pessoa[opc][0]} , {pessoa[opc][1]}')
