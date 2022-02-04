i = h = m = c = s = idade = 0
while True:
    s = cont = ' '
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('Idade: '))
    if i >= 18:
        idade += 1
    while s not in 'MF':
        s = (str(input('Sexo: [M/F] ')).strip().upper())
        if s == 'M':
            h += 1
        if s == 'F' and i < 20:
            m += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
        print('-' * 20)
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idade}')
print(f'Ao todo temos pelo menos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')