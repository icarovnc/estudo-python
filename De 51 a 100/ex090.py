aluno = {}
# aluno = {'Nome': input('Insira o nome do aluno: '), 'Média': float(Input('Insira a média do aluno: '))}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = str('Aprovado')
else:
    aluno['situacao'] = str('Reprovado')
print('_' * 30)
print(f'A média é igual a {aluno["media"]} e a situação é {aluno["situacao"]}')