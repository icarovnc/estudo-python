
numero = int(input('\033[1;36;107m Digite um número para a conversão:\033[m '))
opcao = int(input(' \033[1;35;107m 1 - Para transformar em Binário\033[m '
                  '\n \033[1;34;107m 2 - Para transformar em Octal\033[m'
                  '\n \033[1;33;107m 3 - Para trasnformar em Hexadecimal\033[m '
                  '\n \033[1;33;107m>>>>>>>>>>>>>>>\033[m '))
if opcao == 1:
    conversao = bin(numero)[2:]
elif opcao == 2:
    conversao = oct(numero)[2:]
elif opcao == 3:
    conversao = hex(numero)[2:]
else:
    print('\033[1;31;107mm Número inválido! \033[m')

print(f'\033[1;35;107m O número {numero} convertido para '
      f'a base {opcao} é {conversao}!\033[m ')