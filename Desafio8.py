# definição da função media_numeros
def media_numeros(n):
    # cria a lista numeros
    numeros = []
    # loop que adiciona n números na lista
    for _ in range(0,n):
        num = float(input('Insira um número:'))
        numeros.append(num)
    # cálculo da média
    media = sum(numeros)/len(numeros)
    # imprime a média aritmética dos números
    print(f'A média aritmética dos números é igual a: {media:.3f}')

media_numeros(3)

