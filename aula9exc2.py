def porcentagem_votos(x, y):
    porcentagem = (x / y) * 100
    return porcentagem

windows = 0
Unix = 0
Linux = 0
Netware = 0
mac = 0
outros = 0


print("1- windows")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- mac")
print("6- outros")
print("0- parar votacao")

while True:
    voto = int(input("Qual o melhor sistema operacional: "))
    if voto == 0:
        break

    if voto == 1:
        windows += 1
    elif voto == 2:
        Unix += 1
    elif voto == 3:
        Linux += 1
    elif voto == 4:
        Netware += 1
    elif voto == 5:
        mac += 1
    elif voto == 6:
        outros += 1

    total_votos = windows + Unix + Linux + Netware + mac + outros

print(f"Resultado windows: {windows} votos, {porcentagem_votos(windows, total_votos):.2f}%")
print(f"Resultado Unix: {Unix} votos, {porcentagem_votos(Unix, total_votos):.2f}%")
print(f"Resultado Linux: {Linux} votos, {porcentagem_votos(Linux, total_votos):.2f}%")
print(f"Resultado Netware: {Netware} votos, {porcentagem_votos(Netware, total_votos):.2f}%")
print(f"Resultado Mac: {mac} votos, {porcentagem_votos(mac, total_votos):.2f}%")
print(f"Resultado Outros: {outros} votos, {porcentagem_votos(outros, total_votos):.2f}%")
print(f"Total de votos: {total_votos}")