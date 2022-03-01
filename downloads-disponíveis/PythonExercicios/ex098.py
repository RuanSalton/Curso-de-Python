from time import sleep


def contador(início, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if início < fim:
        for c in range(início, fim + 1, passo):
            print(f'{c} ',end='')
            sleep(0.5)
        print('FIM!')
    elif início > fim:
        for c in range(início, fim - 1, - passo):
            print(f'{c} ',end='')
            sleep(0.5)
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
if passo <= 0:
    passo *= -1
if passo == 0:
    passo = 1
contador(inicio, fim, passo)
