print('\033[7;34;107m CONDIÇÃO PAR A EXISTENCIA DE UM TRIÂNGULO\033[m')
print('\033[7;34;107m DIGITE OS LADOS DO TRIANGULO\033[m')
ra = int(input('\033[7;32;107m Digite o primeiro número:\033[m '))
rb = int(input('\033[7;32;107m Digite o segundo número:\033[m' ))
rc = int(input('\033[7;32;107m Digite o terceiro número:\033[m '))
if ra < rb + rc and rb < ra + rc and rc < ra + rb:
    print('\033[7;35;107mPode formar um triangulo\033[m ')
    if ra == rb == rc:
        forma = '\033[7;35;107mEQUILATERO\033[m'
    elif ra == rb != rc or ra == rc != rb or rb == rc != ra:
        forma = '\033[7;35;107mISÓCELES\033[m'
    elif ra != rb != rc != ra:
        forma = '\033[7;35;107mESCALENO\033[m'
    print(f'\033[7;35;107mO FORMATO DO TRIANGULO SERÁ: {forma}\033[m')
else:
    print('\033[7;35;107m Não podem formar um triangulo\033[m ')