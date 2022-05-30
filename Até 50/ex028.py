import random

nome = str(input('Digite seu nome: '))
pc = str(random.randint(0, 5))
pessoa = str(input('Digite um número de 0 a 5: '))
if pc == pessoa:
    print(f'Parabéns {nome}, você acertou meu número')
else:
    print(f'Meu número foi {pc}, tente novamente {nome}')
print('Ótimo jogo')