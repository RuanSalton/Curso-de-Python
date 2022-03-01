import random
from time import sleep
num = random.randint(0, 5)
guess = int(input('Tente advinhar um numero de 0 a 5: '))
print('Analizando aqui sua resposta...')
sleep(2)
if guess == num:
    print('{}, você acertou, meus parabéns!!'.format(num))
else:
    print('{}, errou, o pc venceu você!'.format(num))
