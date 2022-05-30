n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 > n3:
    print(f'O maior número é o {n1} e o menor é o {n2}')
elif n1 > n3 > n2:
    print(f'O maior número é o {n1} e o menor número é o {n2}')
elif n2 > n3 > n1:
    print(f'O maior número é o {n2} e o menor número é o {n1}')
elif n2 > n1 > n3:
    print(f'O maior número é o {n2} e o menor é o {n3}')
elif n3 > n1 > n2:
    print(f'O maior número é o {n3} e o menor é o {n2}')
elif n3 > n2 > n1:
    print(f'O maior número é o {n3} e o menor é o {n1}')