# programa que consegui sem "ajuda"
'''def funções_python(txt):
    while True:
        função = str(input(txt))
        if função == 'fim':
            print('\033[31;107mAté logo\033[m')
            break
        else:
            print(f"\33[1;31;43m \033[m")
            print(f'\033[34;43m{função}')
            help(função)
            print(f'\033[m]')


função = funções_python('Deseja ver qual função do python? ').strip().upper()
print(função)'''
cores = ('\033[m',          # 0 - sem cor
         '\033[7;30m',      # 1 - branco
         '\033[1;30;41m',   # 2 - vermelho
         '\033[1;30;42m',   # 3 - verde
         '\033[1;30;43m',   # 4 - amarelo
         '\033[1;30;44m',   # 5 - roxo
         '\033[1;30:45m',   # 6 - cinza
         '\033[1;30;46m',   # 7 - magenta
         '\033[1:30;47m',   # 8 - cinza
         )
def título(msg, cor =0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('_' * tamanho)
    print(f'  {msg}')
    print('_' * tamanho)
    print(cores[0], end='')


def ajuda(opt):
    título(f'Acessando manual do comando \'{opt}\'', 5)
    print(cores[7], end='')
    help(opt)
    print(cores[0], end='')


#principal
while True:
    título('Sistema de ajuda python', 4)
    opt = input('Digite um comando: ').strip().lower()
    if opt == 'fim':
        break
    else:
        ajuda(opt)
título('Aprende esse caralhooooo! FIMMM', 3)