L = []
max = 0
count = 0
ind = []

for c in range(9):
    num = int(input('Digite um valor: '))
    L.append(num)

for c in L:
    if c > max:
        max = c

for c in L:
    if c == max:
        count += 1

start = 0
for c in L:
    if c == max:
        dex = L.index(max,start)
        ind.append(dex)
    start += 1


print("-"*30,'\nMaior valor digitado: {}\n\nQuantidade de vezes que apareceu: {}\n\níndicie(s) encontrado: {}'.format(max, count, ind))