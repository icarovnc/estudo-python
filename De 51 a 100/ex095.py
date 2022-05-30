jogador = {}
gol = []
dados = []
while True:
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
    jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
    for c in range(0, jogador['partidas']):
        gol.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    dados.append(jogador.copy())
    opt = str(input('Deseja cadastrar outro jogador?? [S/N] ')).strip().upper()
    while opt not in 'NS':
        opt = str(input('Deseja cadastrar outro jogador?? [S/N] ')).strip().upper()
    if opt == 'N':
        break
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 55)
for k, v in enumerate(dados):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 55)

while True:
    opt = int(input('Mostrar dados de qual jogador?   (999 para parar)'))
    if opt == 999:
        break
    if opt > len(dados):
        print(f'ERRO. NÃO EXISTE JOGADOR {opt}')
    else: 
        print(f'Levantamento do jogador {dados[opt]["nome"]}')
        for i, g in enumerate(dados[opt]['gols']):
            print(f'No {i + 1} para° jogo fez {g} gols')
print(f'-' * 26)