lista = continuar = list()
while True:
    lista += [int(input('Digite um valor: '))]
    continuar = str(input('Continuar? [S/N] ')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('Opção inválida. \nDeseja continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista')