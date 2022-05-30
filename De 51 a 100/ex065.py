media = cont = soma = n = maior = menor =0
c = 'S'
while c == 'S':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if c == 'N':
        print('Programa finalizado')
    elif c != 'S' and c != 'N':
        print('Opção inválida! Tente novamente')
        c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor número foi {menor}')
