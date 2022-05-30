from time import sleep
nome = input('Digite seu nome: ').title()
valor_casa = float(input('Qual o valor da casa que você deseja comprar? '))
salario = float(input('De quanto é o seu salário? '))
anos = int(input('Em quantos anos você deseja pagar essa casa? '))
tempo = anos * 12
sleep(2)
if valor_casa / tempo < (salario / 100) * 30:
    print(f"{nome}, seu empréstimo foi aprovado. O"
          f" valor da prestação será R${valor_casa / tempo:.2f}")
elif valor_casa / tempo > (salario / 100) * 30:
    print(f'{nome}, o empréstimo não foi aprovado porque o valor da prestação '
          f'ultrapassa 30% do seu salário!')