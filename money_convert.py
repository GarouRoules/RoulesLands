# Taxa de câmbio fixa (exemplo)
taxa_cambio = 5.39  # 1 USD = 5 BRL
while True:

    def converter_dolar_para_real(valor_em_dolar):
        valor_em_dolar = valor_em_dolar * taxa_cambio
        return valor_em_dolar

# Exemplo de uso
    valor_em_dolar = float(input("Digite o valor em dolar (USD): $ "))
    valor_em_real = converter_dolar_para_real(valor_em_dolar)
    print(f"Valor em real (BRL): R${valor_em_real:.2f}")

