dias = int(input('Qual a quantidade de dias alugado? '))
km = float(input('Quantos Km foram rodados nesses dias? '))

custodia = dias * 60
custokm = km * 0.15

preco = custodia + custokm
print('O preço a pagar é de R${:.2f}'.format(preco))