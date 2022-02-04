from datetime import date
from datetime import date
temp = {}

temp['nome'] = str(input('Nome: ')).strip().capitalize()
nas = int(input('Ano de nascimento: '))
temp['idade'] = date.today().year - nas
temp['ctps'] = int(input('N° CTPS: (0 não tem) '))
if temp['ctps'] != 0:
    temp['contratação'] = int(input('Ano de contratação: '))
    temp['salario'] = float(input('Salário: R$'))
    temp['aposentadoria'] = temp['contratação'] - nas + 35
print('-=' * 20)
print(temp)
for k, v in temp.items():
    print(f'{k} tem valor {v}')