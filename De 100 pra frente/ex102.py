def fatorial(numero, show=False):
    fat = 1
    if show == True:
        for c in range(numero, 0, -1):
            fat *= c
            print(c, end='')
            print(" X " if c > 1 else " = ", end='')
        return print(fat)
    if show == False:
        for c in range(numero, 1, -1):
            fat *= c
        return print(f'O fatorial de {numero} é {fat}')

n = int(input('Digite o número: '))
opt = input('Deseja ver o cálculo? [S/N] ').strip().upper()
while opt not in 'NS':
    opt = str(input('Opção inválida. \nDeseja ver o cálculo? [S/N] ')).strip().upper()
    if opt == 'N':
        break
if opt == 'S':
        opt = True
else:
    opt = False
fatorial(n, opt)