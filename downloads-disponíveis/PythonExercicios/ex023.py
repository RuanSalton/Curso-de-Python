num = int(input('Digite um numero com 4 dígitos entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} dividido em casas fica:'.format(num))
print('Unidade:{}  Dezena:{}  Centena:{}  Milhar:{}'.format(u, d, c, m))
