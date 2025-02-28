preco = float(input("Digite o preco do produto: "))
origem = int(input("Digite o codigo de origem do produto: "))

if origem >30:
    print(f"Preco: {preco}, Procedencia: importado")
   
elif origem == 1:
     print(f"Preco: {preco}, Procedencia: sul")

elif origem == 2:
     print(f"Preco: {preco}, Procedencia: norte")

elif origem == 3:
    print(f"Preco: {preco}, Procedencia: leste")

elif origem == 4:
     print(f"Preco: {preco}, Procedencia: oeste")

elif origem == 5 or origem == 6:
    print(f"Preco: {preco}, Procedencia: nordeste")

elif origem == 7 or origem == 8 or origem == 9:
    print(f"Preco: {preco}, Procedencia: sudeste")

elif origem >= 10 and origem <=20:
    print(f"Preco: {preco}, Procedencia: centro-oeste")

elif origem >=25 and origem <=30:
    print(f"Preco: {preco}, Procedencia: nordeste")