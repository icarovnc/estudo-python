
preco = float(input('Qual o valor ds compras? R$'))
print('FORMAS DE APGAMENTO')
escolha = int(input('[1] à vista dinheiro/cheque '
      '\n[2] à vista cartão '
      '\n[3] 2x no cartão '
      '\n[4] 3x ou mais no cartão '))
if escolha == 1:
    pagar = (preco / 100) * 10
    print(f'Sua compra de R${preco:.2f} custará R${preco - pagar:.2f} no final')
elif escolha == 2:
    pagar = (preco /100) * 5
    print(f'Sua compra de R${preco:.2f} custará R${preco - pagar:.2f} no final')
elif escolha == 3:
    pagar = preco / 2
    print(f'Sua compra de R${preco:.2f} será divida em 2x de R${pagar:.2f}')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        pagar = preco + ((preco / 100) * 20)
        print(f'Sua compra de R${preco:.2f} custará R${pagar:.2f} será dividida '
              f'em {parcelas}x de R${pagar / parcelas:.2f}')







'''print('Escolha o produto para comprar')
produtos = ['TV', 'JBL', 'Notebook']
escolha = int(input(f'Digite o número do produto que você quer:'
                    f'\n1 - {produtos[0]} '
                    f'\n2 - {produtos[1]} '
                    f'\n3 - {produtos[2]}'
                    f'\n>>>>>>>>>>>> '))
produtos[0] = 2500.56
produtos[1] = 1500.99
produtos[2] = 5000.89

avista = str(input('O pagamento será à vista? (S/N)').strip().upper())  # Define se será a vista
if avista == 'S':
    cartao_ou_dinheiro = str(input('Será no dinheo ou cartão?(D/C)')).strip().upper()
    if cartao_ou_dinheiro == 'D':  # Inicio pagamento feito no dinheiro
        if escolha == 1:
            valor_final = ((produtos[0] / 100) * 10)
            print(f'Você terá um desconto de 10%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[0] - valor_final:.2f}')
        elif escolha == 2:
            valor_final = ((produtos[1] / 100) * 10)
            print(f'Você terá um desconto de 10%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[1] - valor_final:.2f}')
        elif escolha == 3:
            valor_final = ((produtos[2] / 100) * 10)
            print(f'Você terá um desconto de 10%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[2] - valor_final:.2f}')
    elif cartao_ou_dinheiro == 'C':  # inicio pagamento feito no cartao
        if escolha == 1:
            valor_final = ((produtos[0] / 100) * 5)
            print(f'Você terá um desconto de 5%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[0] - valor_final:.2f}')
        elif escolha == 2:
            valor_final = ((produtos[1] / 100) * 5)
            print(f'Você terá um desconto de 5%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[1] - valor_final:.2f}')
        elif escolha == 3:
            valor_final = ((produtos[2] / 100) * 5)
            print(f'Você terá um desconto de 5%: R$ {valor_final:.2f} '
                  f'\nPagará {produtos[2] - valor_final:.2f}')
elif avista == 'N':
    parcelamento = int(input('Deseja parcelar em quantas vezes? '))
    if parcelamento <= 2:  # inicio pagamento menor que 2
        if escolha == 1:
            parcela = produtos[0] / parcelamento
            print(f'Sua compra será de R${produtos[0]:.2f} '
                  f'\nparcelas serão de R${parcela:.2f}.')
        elif escolha == 2:
            parcela = produtos[1] / parcelamento
            print(f'Sua compra será de R${produtos[1]:.2f} '
                  f'\nparcelas serão de R${parcela:.2f}.')
        elif escolha == 3:
            parcela = produtos[2] / parcelamento
            print(f'Sua compra será de R${produtos[2]:.2f} '
                  f'\nparcelas serão de R${parcela:.2f}.')
    elif parcelamento > 2:  # inicio parcelamento maior 2
        if escolha == 1:
            valor_final = ((produtos[0] / 100) * 20) + produtos[0]
            parcela = valor_final / parcelamento
            print(f'Sua parcela será de R$ {parcela:.2f} '
                  f'\nSua compra total custará {valor_final:.2f}')
        elif escolha == 2:
            valor_final = ((produtos[0] / 100) * 20) + produtos[1]
            parcela = valor_final / parcelamento
            print(f'Sua parcela será de R${parcela:.2f}'
                  f'\nSua compra total custará {valor_final:.2f}')
        elif escolha == 3:
            valor_final = ((produtos[0] / 100) * 20) + produtos[2]
            parcela = valor_final / parcelamento
            print(f'Sua parcela será de R${parcela:.2f}'
                  f'\nSua compra total custará {valor_final:.2f}')'''
