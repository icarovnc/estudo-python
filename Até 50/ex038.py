n1 = int(input('\033[1;34;107m Digite um número:\033[m '))
n2 = int(input('\033[1;34;107m Digite outro número:\033[m '))
if n1 > n2:
    print(f'\033[1;35;107m O {n1} é maior\033[m ')
elif n1 < n2:
    print(f'\033[1;35;107m O {n2} é maior\033[m ')
else:
    print('\033[1;35;107mOs números são iguais\033[m ')