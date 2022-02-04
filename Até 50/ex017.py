import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1/2)

print('O valor da hipotenusa é {:.3f}'.format(hip))
print('-' * 20)
print('O valor da hipotenusa é {:.3f}'.format(math.hypot(co, ca)))