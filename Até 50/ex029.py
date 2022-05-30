from time import sleep
vel = float(input('Qual a velocidade do carro? '))
print('ANALISANDO...')
sleep(3)
if vel > 80:
    print('Você está acima da velocidade')
    print(f'SUA MULTA SERÁ DE R$ {(vel - 80) * 7}!')
else:
    print('Muito bem, continue andando devagar"')