numesc = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
for c in range(0, len(numesc)):
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numesc[num]}.')
