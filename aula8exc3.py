lista = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
print(lista)

maior_numero = max(lista)
print(maior_numero)

for indice in range(10):
    if lista[indice] == maior_numero:
        print(indice)
