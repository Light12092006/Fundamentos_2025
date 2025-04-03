lista = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
print(f"Numero: {lista}")

soma_par = 0
for numero in lista:
    if numero %2 == 0:
        soma_par += numero 


print(f"Soma dos pares: {soma_par}")