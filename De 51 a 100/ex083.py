'''lista = str(input('Digite a expressão: '))
if lista.count('(') == lista.count(')'):
    print('Sua expressão é válida')
else:
    print('Expressão inválida')'''

cont = 0
lista2 = str(input('Expressão:'))
for item in lista2:
    if item == '(':
        cont += 1
    elif item == ')':
        cont -=1
print(cont)
if cont > 0 or cont < 0:
    print('Expressão inválida')
else:
    print('Expressão válida')