nota_duz = nota_cem = nota_cinq = nota_vin = nota_dez = nota_cin = nota_dois = nota_um = 0
c = nota = 0
print('=' * 40)
print('{:^40}'.format('BANCO ICARO'))
print('=' * 40)
saque = int(input('Qual valor você quer sacar? '))
while True:
    while saque - 200 >= 0:
        saque -= 200
        nota_duz += 1
    while saque - 100 >= 0:
        saque -= 100
        nota_cem += 1
    while saque - 50 >= 0:
        saque -= 50
        nota_cinq += 1
    while saque - 20 >= 0:
        saque -= 20
        nota_vin += 1
    while saque - 10 >= 0:
        saque -= 10
        nota_dez += 1
    while saque - 5 >= 0:
        saque -= 5
        nota_cin += 1
    while saque - 2 >= 0:
        saque -= 2
        nota_dois += 1
    while saque - 1 >= 0:
        saque -= 1
        nota_um += 1
    break
if nota_duz != 0:
    print(f'Total de {nota_duz} de R$200')
if nota_cem != 0:
    print(f'Total de {nota_cem} de R$100')
if nota_cinq != 0:
    print(f'Total de {nota_cinq} de R$50')
if nota_vin != 0:
    print(f'Total de {nota_vin} de R$20')
if nota_dez != 0:
    print(f'Total de {nota_dez} de R$10')
if nota_cin != 0:
    print(f'Total de {nota_cin} de R$5')
if nota_dois != 0:
    print(f'Total de {nota_dois} de R$2')
if nota_um != 0:
    print(f'Total de {nota_um} de R$1')
print('Fim')

