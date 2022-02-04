def verifica_numero(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f'\033[1;31mDigite um número inteiro válido.\033[m')

num = verifica_numero('Digite um número inteiro: ')
print(f'Você acabou de digitar o numero {num}')
print(type(num))