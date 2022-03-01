preço = float(input('Qual é o preço normal do produto? R$'))
print('Opções de pagamento:')
print('[1] para pagamento á vista no dinheiro/cheque')
print('[2] para pagamento á vista no cartão')
print('[3] para até 2x no cartão')
print('[4] para 3x ou mais no cartão')
opção = int(input('Escolha a opção de pagamento: '))
if opção == 1:
    print('O valor fica em R${:.2f} á vista no dinheiro.'.format(preço - (preço * 10 / 100)))
elif opção == 2:
    print('O valor fica em R${:.2f} á vista no cartão.'.format(preço - (preço * 5 / 100)))
elif opção == 3:
    print('O valor fica no cartão, 2x de R${:.2f}.'.format(preço / 2))
elif opção == 4:
    print('O valor fica no cartão, 3x de R${:.2f}.'.format((preço + (preço * 20 / 100)) / 3))
