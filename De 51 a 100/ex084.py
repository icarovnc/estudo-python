dados = []
princ = []
pesos = []
mais = menos = 0
#dados
while True:
    dados.append(str(input('Nome: ').strip().capitalize()))
    dados.append(float(input('Peso: ')))
    if len(princ) == 0:
        mais = menos = dados[1]
    else:
        if dados[1] > mais:
            mais = dados[1]
        if dados[1] < menos:
            menos = dados[1]
    princ.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida.\nDeseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'Você cadastrou {len(princ)} pessoa{"s" if len(princ) > 1 else ""}')
print(f'O maior peso foi de {mais}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mais:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menos}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menos:
        print(f'[{p[0]}]', end=' ')