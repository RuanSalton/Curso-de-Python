frase = str(input('Digite uma frase: ')).strip().upper() # li a frase tirando os espaços antes e depois e colocando tudo em maiúsculas.
palavras = frase.split() # splitei ela para que ela gere uma lista.
junto = ''.join(palavras) # juntei essa lista para eliminar os espaços entre palavras.
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) - 1, - 1, -1):  # fiz o inverso da string contando de trás pra frente de 1 em 1.
    inverso += junto[letra]'''
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:  # testei se o inverso é a mesma coisa que o junto.
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
