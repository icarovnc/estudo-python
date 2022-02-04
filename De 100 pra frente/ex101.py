def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print('Negado')
    elif idade >= 16 and idade < 18 or idade > 65:
        return print('OPCIONAL')
    else:
        return print('OBRIGATORIO')

ano = int(input('Digite sua data de nascimento: '))
voto(ano)