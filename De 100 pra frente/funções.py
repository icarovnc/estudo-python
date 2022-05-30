
def metade(n = 0, formatada = False):
    numero = n / 2
    return numero if formatada is False else moeda_formatada(numero)


def dobro(n = 0, formatada = False):
    numero = n * 2
    return numero if formatada is False else moeda_formatada(numero)

def aumenta_percent(valor = 0, formatada = False):
    percent = valor + (valor * 10 / 100)
    return percent if formatada is False else moeda_formatada(valor)


def diminui_percent(valor = 0, formatada = False):
    percent = valor - (valor * 23 / 100)
    return percent if formatada is False else moeda_formatada(valor)

def moeda_formatada(valor_em_reais = 0, formatada = False):
    ''' 
    ---> Formata a entrada de moedas para R$
    :param valor_em_reais: recebe o valor float de reais
    :param formatada: se for True ele retorna o valor formatado
    :return: retorna formatado se for verdadeiro
    '''
    if formatada == True:
        return f'R${valor_em_reais:.2f}'.replace('.', ',')
    else:
        return valor_em_reais

def resumo(valor):

   print('-' * 34)
   print('Resumo do valor'.center(34))
   print('-' * 34)
   print(f'Preço analisado: \t{moeda_formatada(valor)}')
   print(f'Dobro do preço: \t{moeda_formatada(dobro(valor), True)}')
   print(f'Metade do preço: \t{moeda_formatada(metade(valor), True)}')
   print(f'Aumento de 10%: \t{moeda_formatada(aumenta_percent(valor), True)}')
   print(f'Diminui 20%: \t\t{moeda_formatada(diminui_percent(valor), True)}')
   print('-' * 34)