fras = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {}'.format(fras.count('A')))
print('A posição que aparece pela primeira vez é: {}'.format(fras.find('A') + 1))
print('Aparece pela última vez na posição: {}'.format(fras.rfind('A') + 1))