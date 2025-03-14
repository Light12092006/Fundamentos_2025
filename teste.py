valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

if parcelas == 1:
    desconto = valor * 0.1
    if valor > 5000:
        desconto = valor * 0.15
    print("Desconto total: %.2f"% desconto)
    valor_final = valor - desconto
    print("Valor final da compra com desconto: %2f"% valor_final)
    valor_parcela = valor_final / parcelas
    print("Cada parcela será de: %.2f"% valor_parcela)

if parcelas == 2 or parcelas == 3: 
    desconto = valor * 0.05
    if valor > 5000:
        desconto = valor * 0.1
    print("Desconto total: %.2f"% desconto)
    valor_final = valor - desconto
    print("Valor final da compra com desconto: %2f"% valor_final)
    valor_parcela = valor_final / parcelas
    print("Cada parcela será de: %.2f"% valor_parcela)
    