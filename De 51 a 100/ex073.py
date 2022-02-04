brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f'Lista de times do brasileirão: {brasileirão}')
print(f'Os 5 primeiros são: {brasileirão[0:5]}')
print(f'Os 4 ultimos são: {brasileirão[-4:]}')
print(f'Times em ordem alfabética: {sorted(brasileirão)}')
print(f'Chapecoense está na posição: {brasileirão.index("Chapecoense") + 1}')
