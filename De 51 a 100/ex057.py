from time import sleep
sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo: [M/F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Tente novamente')
        sleep(2)
print('Fim')