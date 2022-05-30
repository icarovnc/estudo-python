n = c = m = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=-' * 15)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADA! VOLTE SEMPRE')
        break
    else:
        while c < 10:
            c += 1
            m = n * c
            print(f'{n} X {c} = {m}')