dis = float(input('Qual a distancia da viagem? '))
if dis <= 200:
    print(f'Via viagem é curta, então o valor da sua passagem é de R$ {dis * 0.50 :.2f}')
else:
    print(f'Sua viagem é longa, então o valor da sua passagem é de R$ {dis * 0.45 :.2f}')