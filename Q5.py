lista=[]
print("Informe os 10 números: ")
for c in range(0,10):
    lista.append(int(input("{}º Número: \n".format(c+1))))

print("-"*30)
lista.sort()
print("Ordem crescente: {}.".format(lista))
lista.sort(reverse=True)
print("Ordem decrescente: {}.".format(lista))

