import math
ang = int(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do seno de {} é {:.2f}.'.format(ang, seno))
print('O valor do coseno de {} é {:.2f}.'.format(ang, cos))
print('A tangente de {} é {:.2f}.'.format(ang, tan))
