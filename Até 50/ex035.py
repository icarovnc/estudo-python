print('CONDIÇÃO PAR A EXISTENCIA DE UM TRIÂNGULO')
print('DIGITE OS LADOS DO TRIANGULO')
ra = int(input('Digite o primeiro lado: '))
rb = int(input('Digite o segundo lado: '))
rc = int(input('Digite o terceiro lado: '))
if ra < rb + rc and rb < ra + rc and rc < ra + rb:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')