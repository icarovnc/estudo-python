futebol = {}
gol = []
futebol['jogador'] = str(input('Nome do jogador: ')).strip().capitalize()
futebol['partidas'] = int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
for c in range(0, futebol['partidas']):
    gol.append(int(input(f'Quantos gols na partida {c + 1}: ')))
futebol['gols'] = gol
futebol['total'] = sum(gol)
print('-=' * 30)
print(futebol)
print('-=' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {futebol["jogador"]} jogou {futebol["partidas"]} partidas')
for c in range(0, futebol['partidas']):
    print(f'    => Na partida {c + 1}, fez {gol[c]}')
print(f'Foi um total de {sum(gol)} gols')