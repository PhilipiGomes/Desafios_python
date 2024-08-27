# Declara a variável e pede ao usuário que escreva um valor float para a ser efetuada a conversão de dólar para reais.
dolar = float(input('Insira o valor em dólar: '))

# Realiza a conversão do valor em dólar para reais.
real = dolar*5.49

# Imprime a conversão do valor em dólar para reais.
print(f'| O valor convertido para reais é: R${real:.2f} |')
