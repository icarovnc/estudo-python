nome = str(input('Digite seu nome completo: '))
primeiro = nome.split()
ultimo = len(primeiro) -1
print('O primeiro nome é {}'.format(primeiro[0]))
print('O ultimo nome é {}'.format(primeiro[ultimo]))