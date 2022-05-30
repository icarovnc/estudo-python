extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'cartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '
while True:
    numero = int(input('Digite um número: '))
    if numero < 0 or numero > 20:
        print('Opção inválida. Tente novamente')
        continue
    print(f'O número por extenso é {extenso[numero]}')
    continuar = str(input('Deseja outro número por extenso? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('Tente novamente')
        continuar = str(input('Deseja outro número por extenso? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('FIM')
