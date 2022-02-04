from random import randint
c = tot = v = 0
while True:
    n = int(input('Diga um valor: '))
    pc = randint(0, 10)
    tot = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o PC jogou {pc}. Total de {tot}')
    if tipo == 'P':
        if n % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if n % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            c += 1
            break
print(f'GAME OVER! Você venceu {v} vezes')