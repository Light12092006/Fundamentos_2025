lista = []


quantidade = int(input("DIgite a quantidade de numeros: "))

for i in range(quantidade):
    nmr = int(input("DIgite um numero:"))
    lista.append(nmr)

for i in range(nmr, -1, -1):
    print(lista[i])
