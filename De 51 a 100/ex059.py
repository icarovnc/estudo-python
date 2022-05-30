'''from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('[1] somar'
          '\n[2] multiplicar'
          '\n[3] maior'
          '\n[4] novos números'
          '\n[5] sair do programa')
sair = int(input('>>>> Qual é a sua opção? '))
result = 0
while sair != 5:
    if sair == 1:
        result = n1 + n2
        print(f'A soma entre {n1} e {n2} é {result}')
        print('=-' * 15)
        sleep(2)
        print('[1] somar'
              '\n[2] multiplicar'
              '\n[3] maior'
              '\n[4] novos números'
              '\n[5] sair do programa')
        sair = int(input('>>>> Qual é a sua opção? '))
    elif sair == 2:
        result = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {result}')
        print('=-' * 15)
        sleep(2)
        print('[1] somar'
              '\n[2] multiplicar'
              '\n[3] maior'
              '\n[4] novos números'
              '\n[5] sair do programa')
        sair = int(input('>>>> Qual é a sua opção? '))
    elif sair == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('=-' * 15)
            sleep(2)
            print('[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa')
            sair = int(input('>>>> Qual é a sua opção? '))
        if n1 == n2:
            print(f'{n1} é igual que {n2}')
            print('=-' * 15)
            sleep(2)
            print('[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa')
            sair = int(input('>>>> Qual é a sua opção? '))
        else:
            print(f'{n2} é maior que {n1}')
            print('=-' * 15)
            sleep(2)
            print('[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa')
            sair = int(input('>>>> Qual é a sua opção? '))
    elif sair == 4:
        print('Digite novos números: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        print('=-' * 15)
        sleep(2)
        print('[1] somar'
              '\n[2] multiplicar'
              '\n[3] maior'
              '\n[4] novos números'
              '\n[5] sair do programa')
        sair = int(input('>>>> Qual é a sua opção? '))
    else:
        if sair > 5:
            print('Opção inválida')
            print('=-' * 15)
            print('[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa')
            sair = int(input('>>>> Qual é a sua opção? '))
print('Finalizando....')
sleep(2)
print('Fim do programa! Volte sempre')'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
sair = False
soma = n1 + n2
mult = n1 * n2
while not sair:
    menu = int(input('[1] somar'
         '\n[2] multiplicar'
         '\n[3] maior'
         '\n[4] novos números'
         '\n[5] sair do programa'
                     '\n>>>> Qual a sua opção?  '))
    if menu == 1:
        print(f'A soma entre os números é {soma}')
        print('-=' * 10)
    if menu == 2:
        print(f'A multiplicação entre os números é {mult}')
        print('-=' * 10)
    if menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('-=' * 10)
        else:
            print(f'{n2} é maior que {n1}')
            print('-=' * 10)
    if menu == 4:
        n1 = int(input('Insira o novo valor 1: '))
        print('-=' * 10)
        n2 = int(input('Insira o novo valor 2: '))
        print('-=' * 10)
    if menu == 5:
        print('Entendido, estamos finalizando o programa! Tchauzinho! :)')
        sair = True
        print('-=' * 10)
    if menu > 5:
        print('Informe uma opção válida')
        print('-=' * 10)