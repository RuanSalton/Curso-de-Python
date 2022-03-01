print('Vamos ver a tabuada.')
num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} X {:>2} = {:>2}'.format(num, c, num * c))
