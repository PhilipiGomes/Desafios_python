# Declara a variável e pede ao usuário que escreva um valor float para a temperatura em Fahrenheit.
t_f = float(input('Insira a temperatura em Fahrenheit: '))

# Realiza a conversão de Fahrenheit para Celsius.
t_c = (t_f-32)*(5/9)

# Imprime a conversão da temperatura de Fahrenheit para a temperatura em Celsius.
print(f'| A temperatura em graus Celsius é: {t_c:.2f} |')
