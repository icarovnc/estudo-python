preco = float(input('Qual o preço do produto? '))
porcent = preco * (5/100)
desc = preco - porcent

print('O novo preço com desconto é {}'.format(desc))