import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
print('*' * 20)



nomes = ['Flávio', 'Ícaro', 'Fernando', 'Gabriel']
def selectRamdom(nomes):
    return random.choice(nomes)

print('Será sorteado aleatoriamento o nome do aluno.')
print('-' * 20)
print('O aluno escolhido é:', selectRamdom(nomes))

