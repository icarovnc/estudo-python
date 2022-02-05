import funções

p = input('Digite um valor: R$')
print(f'O dobro de R${p} é igual a R${funções.dobro(p)}')
print(f'A metade de R${p} é igual a R${funções.metade(p)}')
print(f'Aumentando 10% de R${p} fica {funções.aumenta_percent(p)}')
print(f'Diminui 23% de R${p} fica {funções.aumenta_percent(p)}')