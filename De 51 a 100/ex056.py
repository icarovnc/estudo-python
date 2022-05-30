somaidade = 0
media = 0
velho = 0
nomevelho = 0
nova = 0
cont = 0
for analisador in range (1, 5):
    print(f'----- {analisador}º Pessoa ----- ')
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F] ')).strip().upper()
    somaidade += idade
    media = somaidade / analisador

    if sexo == 'F':
        if idade < 20:
            nova =+ 1
    if sexo == 'M':
        if analisador == 1:
            velho = idade
            nomevelho = nome
        if idade > velho:
            velho = idade
            nomevelho = nome
print(f'A média de idade do grupo é {media}')
print(f'O homem mais velho tem {velho} anos e se chama {nomevelho}')
print(f'O total de mulheres abaixo de 20 anos: {nova}')