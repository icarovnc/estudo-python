
salario = float(input('Digite seu salário: R$ '))
audez = (10 / 100) * salario
auquin = (15 / 100) * salario
if salario >= 1250:
    print(f'Seu salário de R$ {salario:.2f} terá um aumento de 10% e passará a ser R$ {audez + salario}')
else:
    print(f'Seu salário de R$ {salario:.2f} terá um aumento de 15% e passará a ser R% {auquin + salario}' )