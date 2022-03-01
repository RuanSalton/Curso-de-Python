l = float(input('Qual é a largura da parede? '))
h = float(input('Qual é a altura da parede? '))
a = l * h
t = a / 2
print('A parede tem {:.2f}m² de área, são {:.2f}L de tinta para pintá-la.'.format(a, t))
