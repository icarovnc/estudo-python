altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

litro = area / 2


print('A quantidade de litros de tinta para a parede é de {}m²'.format(litro))
print('========================================================')
print('A quantidade de litros de tinta para a parede é de  {}m²'.format((altura * largura)/2))