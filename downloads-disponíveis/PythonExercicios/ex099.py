from time import sleep
def maior(* num):
    print('-=' * 30)
    print('Analizando os valores passados...')
    n = mai = 0
    while n < len(num):
        print(f'{num[n]} ',end='')
        sleep(0.5)
        if n == 0:
            mai = num[n]
        elif num[n] > mai:
            mai = num[n]
        n += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')



# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
