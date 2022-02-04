cmil = prod = prec = totcom = mbarato = c = 0
prodmb = ' '
print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
while True:
    prod = str(input('Nome do produto: '))
    prec = float(input('Preço do produto: '))
    totcom += prec
    c += 1
    if c == 1 or prec < mbarato:
        mbarato = prec
        prodmb = prod
    '''else:
        if prec < mbarato:
            mbarato = prec
            prodmb = prod'''
    if prec > 1000:
        cmil += 1
    cont = ' '
    while cont not in 'SN':
        print('_' * 40)
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break
print('_' * 20)
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'O total de compa foi R${totcom:2f}')
print(f'Temos {cmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prodmb} que custa {mbarato}')
