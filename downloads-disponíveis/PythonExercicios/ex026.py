frase = str(input('Digite uma frase: ')).strip().upper()
print('Em "{}" a letra "A" aparece {} vezes.'.format(frase, frase.count('A')))
print('A letra "A" aparece pela primeira vez em {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez em {}.'.format(frase.rfind('A')+1))
