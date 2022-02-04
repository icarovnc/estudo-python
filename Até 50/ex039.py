from datetime import date

nome = str(input('\033[1;35;107m Informe seu nome:\033[m ')).title()
nascimento = int(input('\033[1;35;107m Informe seu ano de nascimento:\033[m '))
idade = date.today().year - nascimento
if idade < 18:
    alistamento = f'\033[1;34;107m{nome}, ainda irá se alistar. ' \
                  f'Faltam {18 - idade} anos para se alistar\033[m '
elif idade == 18:
    alistamento = f'\033[1;34;107m{nome}, está na hora de se alistar\033[m '
elif idade > 18:
    alistamento = f'\033[1;34;107m{nome}, você está atrasado para se alistar. ' \
                  f'\nEstá com {idade - 18} anos de atraso. \033[m'
print(alistamento)