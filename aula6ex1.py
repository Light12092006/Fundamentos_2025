quantidade = int(input("Digite a quantidade de numeros a serem testados: "))

quantidade_primos = 0

for i in range(quantidade):
    numero = int(input(f"Digite o numero {i + 1}: "))

    a = 0
    for j in range(1,numero + 1):
        if numero % j == 0:
            a +=1
    if a == 2:
        quantidade_primos +=1
print(f"vc digitou {quantidade_primos} numeros primos de {numero} numeros")
        