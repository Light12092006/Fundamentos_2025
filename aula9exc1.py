intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    nmr = int(input("Digite um numero: "))
    if nmr < 0 or nmr > 100:
        break

if nmr >=  0 or nmr <= 25:
    intervalo_0_25 +=1
elif nmr >= 26 or nmr <= 50:
    intervalo_26_50 +=1

elif nmr >= 51 or nmr <= 75:
    intervalo_51_75 +=1

elif nmr >= 76 or nmr <=100:
    intervalo_76_100 +=1

print(f"Numeros no intervalo de 0 a 25: {intervalo_0_25}")
print(f"Numeros no intervalo de 26 a 50: {intervalo_26_50}")
print(f"Numeros no intervalo de 51 a 75: {intervalo_51_75}")
print(f"Numeros no intervalo de 76 a 100: {intervalo_76_100}")