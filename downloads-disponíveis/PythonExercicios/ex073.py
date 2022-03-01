tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
          'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
          'Ceará SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá',
          'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('-=' * 20)
print(f'Tabela dos times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=' * 20)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('-=' * 20)
print('A Chapecoense está na {}ª posição.'.format((tabela.index('Chapecoense'))+ 1))
