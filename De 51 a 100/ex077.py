tupla = 'aprender', 'tecnologia', 'python', 'erika', 'icaro'
vogais = 'aeiou'
print(tupla)
a = 0
for palavra in tupla:
        print(f'\nNa palavra {palavra.upper()} temos: ', end='')
        for vogal in vogais:
                if vogal in palavra:
                        print(f'{vogal.upper()} ', end= '')
print('.')