lista = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
print(f"Numero: {lista}")

for numero in range(10):
    if numero %2 == 0:
        soma_par = numero +numero
        print(f"Soma dos pares: {soma_par}")

