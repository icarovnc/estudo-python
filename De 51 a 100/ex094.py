dados = {}
lista = []
mulheres = []
media = soma = 0
while True:
    #cadastra dados e verifica se opções são válidas
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Opção inválida. \nSexo: [M/F] ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    opt = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()
    while opt not in 'NS':
        opt = str(input('Opção inválida. \nDeseja cadastrat outra pessoa? [S/N] ')).strip().upper()
    if opt == 'N':
        break
print('-=' * 20)

media = soma / len(lista)
print(lista)
#printa os dados colhidos
print(f'- Foram cadastradas {len(lista)} pessoas')
print(f'- A média de idade do grupo: {media:5.2f} anos')
print(f'- As mulheres cadastradas foram: ', end=', ')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'{lista[c]["nome"]}')
print(f'- Pessoas com a idade acima da media:')
for v in range(0, len(lista)):
    if lista[v]['idade'] >= media:
        print(f'Nome: {lista[v]["nome"]}, idade: {lista[v]["idade"]}, sexo: {lista[v]["sexo"]}')