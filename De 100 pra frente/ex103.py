def ficha(nome = '<desconhecido>', gols = ''):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isdigit():
        gols = 0
    return print(f'O jogador {nome} fez {gols} gols')

print('_' * 30)
nome = str(input('Nome do jogador: '))
gols = input('Quantidade de gols que ele marcou: ')
ficha(nome, gols)