#Elabore um programa utilizando vetores para armazenar 10 números e ao final escreva a quantidade de números negativos,
#positivos e nulos.
listanum = []
negativo = 0
positivo = 0
nulo = 0
cont = 1
for c in range(0,10):
    listanum.append(float(input(f"Digite o {c+1}º número: ")))
    if listanum[c] == 0:
        nulo = nulo + 1
    elif listanum[c] < 0:
        negativo = negativo + 1
    else:
        positivo = positivo + 1
print(f'Foram digitados {negativo} números negativos!')
print(f'Foram digitados {positivo} números positivos!')
print(f'Foram digitados {nulo} números nulos!')