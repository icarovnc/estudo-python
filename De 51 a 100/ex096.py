def area(a, b):
    ar = a * b
    print(f'Seu terreno de {a}m X {b}m tem área de {ar}m')

print(' CONTROLE DE TERRENOS ')
print('-' * 30)
area(a = float(input('LARGURA(m) ')), b =(float(input('COMPRIMENTO(m) '))))